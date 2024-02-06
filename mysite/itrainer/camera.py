import cv2 as cv
import numpy as np

class VideoCamera(object):
    def __init__(self):
        self.video = cv.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        ret, image = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        if ret:
            frame_flip = cv.flip(image, 1)
        else:
            frame_flip = np.zeros((480, 640, 3), dtype=np.uint8)
            
        _, jpeg = cv.imencode(".jpg", frame_flip)
        return jpeg.tobytes()