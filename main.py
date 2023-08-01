import pygame
from config.setup import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from classes.game import Game

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Thumb Driver!")
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
game = Game()

exit = False
it = 1
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    if it <= 500 and it % 100 == 0:
        game.accelerate()

    if it % 64 == 0:
        game.create_obstacle()

    game.draw_screen(screen)
    clock.tick(FPS)
    it += 1

pygame.quit()
