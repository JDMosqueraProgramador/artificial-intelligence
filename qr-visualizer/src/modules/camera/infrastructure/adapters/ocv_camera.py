import cv2
import numpy as np
from pyzbar.pyzbar import decode
from modules.camera.domain.ports.camera_port import ICamera
import threading
import time

class Camera(ICamera):
    def __init__(self):
        self.font = cv2.FONT_HERSHEY_PLAIN
        self.color = (0, 255, 0)
        self.width = 640
        self.height = 480
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, self.width)
        self.cap.set(4, self.height)
        self.read_cache = []

        def set_interval(func, sec):
            def func_wrapper():
                set_interval(func, sec)
                func()
            t = threading.Timer(sec, func_wrapper)
            t.start()
            return t
        
        set_interval(self.clear_cache, 10)

    def clear_cache(self):
        self.read_cache = []

    async def read_camera(self):
        while True:
            _, raw_img = self.cap.read()
            img, decode_data = await self.read_qr(raw_img)
            cv2.imshow('img', img)
            cv2.waitKey(1)

    async def read_qr(self, img):
        img_with_filters = self.apply_filters(img)
        decode_data = await self.decode_qrs(
            img=img_with_filters, 
            img_without_filters=img
        )

        return img, decode_data

    def apply_filters(self, img):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        return img

    async def decode_qrs(self, img, img_without_filters):
        decode_data = []
        for barcode in decode(img):
            decoded_data = barcode.data.decode('utf-8')
            is_repeat = decoded_data in self.read_cache

            self.__print_polyline_in_code(
                img=img_without_filters, 
                polygon=barcode.polygon, 
                data=decoded_data, 
                is_repeat=is_repeat
            )

            if is_repeat:
                break
            
            self.read_cache.append(decoded_data)
            decode_data.append(decoded_data)
        
        return decode_data

    def __print_polyline_in_code(self, img, polygon, data, is_repeat=False):
        points = np.array([polygon], np.int32)
        points = points.reshape((-1, 1, 2))

        color = self.color if is_repeat else (255, 0, 0)  

        cv2.polylines(
            img, 
            pts=[points], 
            isClosed=True, 
            color=color, 
            thickness=3
        )

        text = 'Already read, data: ' + data if is_repeat else 'New, data: ' + data
        cv2.putText(img, text, (50, 50), self.font, 2, color, 3)

        if not is_repeat:
            cv2.imshow('Taken QR', img)
            time.sleep(1)
            cv2.destroyWindow('Taken QR')
