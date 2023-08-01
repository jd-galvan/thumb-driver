import pygame
from config.setup import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from classes.game import Game

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Thumb Driver!")
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
game = Game()

exit = False
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    # screen.fill((0, 0, 0))
    game.draw_screen(screen)
    clock.tick(FPS)

pygame.quit()
