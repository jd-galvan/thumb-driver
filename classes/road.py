import pygame
from config.setup import INITIAL_VELOCITY, INCREASING_FACTOR_SPEED

IMG = pygame.image.load("./images/road.jpeg")


class Road(object):
    def __init__(self) -> None:
        self.backgrounds = [
            {
                "image": IMG,
                "x_position": 0
            },
            {
                "image": IMG,
                "x_position": IMG.get_width()
            },
            {
                "image": IMG,
                "x_position": IMG.get_width() * 2
            }
        ]

        self.velocity = INITIAL_VELOCITY

    def draw(self, screen):
        for b in self.backgrounds:
            screen.blit(b["image"], [b["x_position"], 0])
            if b["x_position"] <= b["image"].get_width() * -1:
                b["x_position"] = abs(b["x_position"]) * 2
            b["x_position"] -= self.velocity

    def increase_speed(self):
        self.velocity += INCREASING_FACTOR_SPEED
