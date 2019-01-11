import numpy as np
import cv2

class Person():
    def __init__(self, image):
        self.image = image
        self.face = None
        self.eye_left = None
        self.eye_right = None
        self.gaze = None
    
    def is_valid(self):
        if self.face is not None:
            if self.eye_left is not None and self.eye_right is not None:
                return True
