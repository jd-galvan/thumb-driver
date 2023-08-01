import pygame
from .road import Road
from .car import Car
from .obstacle import Obstacle
from .gesture import GestureRecognition
import random
from config.setup import SCREEN_HEIGHT, SCREEN_WIDTH
from config.constants import OPEN_PALM


class Game(object):
    def __init__(self):
        self.road = Road()
        self.car = Car()
        self.all_sprites = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()
        self.all_sprites.add(self.car)
        self.gesture_recognition = GestureRecognition()
        self.game_over = False
        self.game_over_text = pygame.font.SysFont("serif", 25).render(
            "Game Over...", True, (255, 255, 255))

    def draw_screen(self, screen):
        self.all_sprites.update()
        self.obstacle_hit_group = pygame.sprite.spritecollide(
            self.car, self.obstacles, True)
        for o in self.obstacle_hit_group:
            self.all_sprites.remove(self.car)
            self.car.kill()
            self.game_over = True

        video_frame = self.gesture_recognition.get_video_image()
        gesture = self.gesture_recognition.detect_gesture()

        if self.game_over:
            pygame.draw.rect(
                screen, (0, 0, 0), (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
            screen.blit(self.game_over_text, [
                        (SCREEN_WIDTH // 2 - self.game_over_text.get_width() // 2),
                        (SCREEN_HEIGHT // 2)])
        else:
            if gesture is not None:
                self.car.change_rail(gesture)
            self.road.draw(screen)
            self.all_sprites.draw(screen)

            for o in self.obstacles:
                o.move()

        screen.blit(video_frame, (0, 0))
        pygame.display.flip()

    def move_car(self, direction):
        self.car.change_rail(direction)

    def accelerate(self):
        self.road.increase_speed()
        for o in self.obstacles:
            o.set_velocity(self.road.get_speed())

    def create_obstacle(self):
        obstacle = Obstacle(SCREEN_WIDTH,
                            random.choice([180, 420]), self.road.get_speed())
        self.all_sprites.add(obstacle)
        self.obstacles.add(obstacle)
