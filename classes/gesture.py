import cv2
import numpy as np
import pygame
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from config.constants import UP, DOWN

POSITIONS = {
    "Thumb_Up": UP,
    "Thumb_Down": DOWN
}


class GestureRecognition:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        base_options = python.BaseOptions(
            model_asset_path='./mediapipe/models/gesture_recognizer.task')
        options = vision.GestureRecognizerOptions(base_options=base_options)
        self.recognizer = vision.GestureRecognizer.create_from_options(options)

    def get_video_image(self):
        success, image = self.cap.read()
        if not success:
            print("Ignoring empty camera frame.")

        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image)
        self.recognition_result = self.recognizer.recognize(mp_image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        frame = cv2.resize(image, (180, 110))
        frame = np.rot90(frame)

        return pygame.surfarray.make_surface(frame)

    def detect_gesture(self):

        if len(self.recognition_result.gestures) > 0:
            try:
                score = self.recognition_result.gestures[0][0].score
                category_name = self.recognition_result.gestures[0][0].category_name
            except:
                print("No gesture detected.")

            if score > 0.65 and category_name in POSITIONS:
                return POSITIONS[category_name]

        return None
