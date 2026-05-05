### this program is a llama game for playing

import pygame
import time
import random

pygame.init()

screen_x = 750
screen_y = 800

screen = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption("Car Vroom game")

game_icon = pygame.image.load("game_icon.png")
pygame.display.set_icon(game_icon)

pygame.display.update()


quit_game = False
score = 0
high_score = 0
textx = 10
texty = 10
font = pygame.font.Font("freesansbold.ttf", 20)


def message(msg, txt_colour, bkgd_colour):
    """Return the color and font values of the text."""
    txt = font.render(msg, True, txt_colour, bkgd_colour)
    text_box = txt.get_rect(center=(144, 256))
    screen.blit(txt, text_box)

def show_score(x, y):
    """Return the lattuide and landutude values of the text."""
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    hi_text = font.render("High: " + str(high_score), True, (255, 255, 255))
    screen.blit(score_text, (x, y))
    screen.blit(hi_text, (x, y + 25))

while not quit_game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True
        
        
    show_score(textx, texty)
    pygame.display.update()


pygame.quit()
quit()