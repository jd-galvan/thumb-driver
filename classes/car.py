import pygame

Y_POSITIONS = {
    "UP": 190,
    "DOWN": 430
}


class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./images/car.png")
        self.rect = self.image.get_rect()
        self.rect.x = 30
        self.rect.y = Y_POSITIONS["UP"]

    def change_rail(self, direction):
        self.rect.y = Y_POSITIONS[direction]
