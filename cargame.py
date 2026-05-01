### this program is a llama game for playing

import pygame
import time
import random

pygame.init()

screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("Car Vroom game")

game_icon = pygame.image.load("game_icon.png")
pygame.display.set_icon(game_icon)


pygame.quit()
quit()