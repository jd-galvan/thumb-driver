import pygame
from .road import Road
from .car import Car
from .obstacle import Obstacle
from .gesture import GestureRecognition
import random
from config.setup import OBSTACLE_WIDTH


class Game(object):
    def __init__(self):
        self.road = Road()
        self.car = Car()
        self.all_sprites = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()
        self.all_sprites.add(self.car)
        for _ in range(5):
            obstacle = Obstacle(random.randrange(1440, 3000, OBSTACLE_WIDTH),
                                random.choice([180, 420]))
            self.all_sprites.add(obstacle)
            self.obstacles.add(obstacle)

        self.gesture_recognition = GestureRecognition()

    def draw_screen(self, screen):
        self.road.draw(screen)
        self.all_sprites.draw(screen)

        for o in self.obstacles:
            o.move()

        video_frame = self.gesture_recognition.get_video_image()
        screen.blit(video_frame, (0, 0))
        direction = self.gesture_recognition.detect_gesture()
        if direction is not None:
            self.car.change_rail(direction)
        pygame.display.flip()

    def move_car(self, direction):
        self.car.change_rail(direction)

    def accelerate(self):
        self.road.increase_speed()
        for o in self.obstacles:
            o.increase_velocity()
