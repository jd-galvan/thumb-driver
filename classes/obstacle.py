import pygame
from config.setup import INITIAL_VELOCITY, INCREASING_FACTOR_SPEED, OBSTACLE_WIDTH, OBSTACLE_HEIGHT


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("./images/rock.png")
        self.image = pygame.transform.scale(
            self.image, [OBSTACLE_WIDTH, OBSTACLE_HEIGHT])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity = INITIAL_VELOCITY

    def move(self):
        self.rect.x -= self.velocity

    def increase_velocity(self):
        self.velocity += INCREASING_FACTOR_SPEED
