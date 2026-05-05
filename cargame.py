### this program is a llama game for playing

import pygame
import time
import random

pygame.init()

screen_x = 750
screen_y = 800
quit_game = False

screen = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption("Car Vroom game")

game_icon = pygame.image.load("game_icon.png")
pygame.display.set_icon(game_icon)

pygame.display.update()

while not quit_game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True


pygame.quit()
quit()