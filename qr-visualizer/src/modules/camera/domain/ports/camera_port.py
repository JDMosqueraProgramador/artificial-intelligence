from abc import ABC, abstractmethod

class ICamera(ABC): 
    @abstractmethod
    def read_camera(self):
        pass

    @abstractmethod
    def read_qr(self):
        pass

    @abstractmethod
    def apply_filters(self, img):
        pass

    @abstractmethod
    def decode_qrs(self, img, img_without_filters):
        pass