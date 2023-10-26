import cv2
import numpy as np
from pyzbar.pyzbar import decode
import time 
from modules.camera.domain.ports.camera_port import ICamera

class Camera(ICamera):
    def __init__(self):
        self.font = cv2.FONT_HERSHEY_PLAIN
        self.color = (0, 255, 0)
        self.width = 640
        self.height = 480
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, self.width)
        self.cap.set(4, self.height)

    def read_camera(self):
        while True:
            _, raw_img = self.cap.read()
            img, decode_data = self.read_qr(raw_img)
            cv2.imshow('img', img)
            cv2.waitKey(1)

    def read_qr(self, img):
        img = self.apply_filters(img)
        decode_data = self.decode_qrs(img)

        return img, decode_data

    def apply_filters(self, img):
        # img = cv2.medianBlur(img, 25) 
        # img = cv2.resize(img, (512, 512), interpolation=cv2.INTER_AREA)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        return img

    def decode_qrs(self, img):
        decode_data = []
        for barcode in decode(img):
            decoded_data = barcode.data.decode('utf-8')
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
