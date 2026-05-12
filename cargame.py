### this program is a llama game for playing

import pygame
import time
import random

pygame.init()

# Screen Size and Screen Create
screen_x = 750
screen_y = 800
screen = pygame.display.set_mode((screen_x, screen_y))

#Icon and Caption
pygame.display.set_caption("Car Vroom game")
game_icon = pygame.image.load("game_icon.png")
pygame.display.set_icon(game_icon)
pygame.display.update()

#Colors
gray = (140, 140, 140)

quit_game = False
score = 0
high_score = 0
textx = 10
texty = 10
car_x = 300
car_y = 650
car_h = 95 
car_w = 150
car_x_change = 0
car_y_change = 0
font = pygame.font.Font("freesansbold.ttf", 20)

# Text create
def message(msg, txt_colour, bkgd_colour):
    """Return the color and font values of the text."""
    txt = font.render(msg, True, txt_colour, bkgd_colour)
    text_box = txt.get_rect(center=(144, 256))
    screen.blit(txt, text_box)

#Score Create
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
    
    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                car_x_change = -20
                car_y_change = 0
            elif event.key == pygame.K_RIGHT:
                car_x_change = 20
                car_y_change = 0

    car_x += car_x_change
    car_x == 0
    car_y += car_y_change
    

    screen.fill(gray)
    show_score(textx, texty)

    car = pygame.Rect(car_x, car_y, car_h, car_w)
    carimage = pygame.image.load("car_1.png").convert_alpha()
    resized_car = pygame.transform.smoothscale(carimage, [car_h, car_w])
    screen.blit(resized_car, car)
    pygame.display.update()

    


pygame.quit()
quit()