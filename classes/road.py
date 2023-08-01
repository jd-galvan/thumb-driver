import pygame

INITIAL_VELOCITY = 3
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
            }
        ]

        self.velocity = INITIAL_VELOCITY

    def draw(self, screen):
        for b in self.backgrounds:
            screen.blit(b["image"], [b["x_position"], 0])
            if b["x_position"] == b["image"].get_width() * -1:
                b["x_position"] = abs(b["x_position"])
            b["x_position"] -= self.velocity

    def increase_speed(self):
        self.velocity += 1
