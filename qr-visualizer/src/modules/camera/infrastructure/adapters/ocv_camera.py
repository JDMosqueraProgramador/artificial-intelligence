import cv2
import numpy as np
from pyzbar.pyzbar import decode
from modules.camera.domain.ports.camera_port import ICamera
import threading

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
        img = self.apply_filters(img)
        decode_data = await self.decode_qrs(img)

        return img, decode_data

    def apply_filters(self, img):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        return img

    async def decode_qrs(self, img):
        decode_data = []
        for barcode in decode(img):
            decoded_data = barcode.data.decode('utf-8')

            if decoded_data in self.read_cache:
                break
            
            self.read_cache.append(decoded_data)
            decode_data.append(decoded_data)

            self.__print_polyline_in_code(img, barcode.polygon, decoded_data)
        
        return decode_data

    def __print_polyline_in_code(self, img, polygon, data):
        points = np.array([polygon], np.int32)
        points = points.reshape((-1, 1, 2))

        cv2.polylines(
            img, 
            pts=[points], 
            isClosed=True, 
            color=self.color, 
            thickness=5
        )

        cv2.putText(img, data, (50, 50), self.font, 2, self.color, 3)
