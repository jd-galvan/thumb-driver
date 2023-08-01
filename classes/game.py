import pygame
from .road import Road
from .car import Car
from .gesture import GestureRecognition


class Game(object):
    def __init__(self):
        self.road = Road()
        self.car = Car()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.car)
        self.gesture_recognition = GestureRecognition()

    def draw_screen(self, screen):
        self.road.draw(screen)
        self.all_sprites.draw(screen)
        video_frame = self.gesture_recognition.get_video_image()
        screen.blit(video_frame, (0, 0))
        direction = self.gesture_recognition.detect_gesture()
        if direction is not None:
            self.car.change_rail(direction)
        pygame.display.flip()

    def move_car(self, direction):
        self.car.change_rail(direction)
