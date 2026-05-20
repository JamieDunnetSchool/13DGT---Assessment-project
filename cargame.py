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
cars_y = 650
cars_x = 150
car_x_change = 0
car_y_change = 0
font = pygame.font.Font("freesansbold.ttf", 20)

# Text create
def message(msg, txt_colour, bkgd_colour):
    """Return the color and font values of the text."""
    txt = font.render(msg , True, txt_colour, bkgd_colour)
    text_box = txt.get_rect(center=(144, 256))
    screen.blit(txt, text_box)

#Score Create
def show_score(x, y):
    """Return the lattuide and landutude values of the tQext."""
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    hi_text = font.render("High: " + str(high_score), True, (255, 255, 255))
    screen.blit(score_text, (x, y))
    screen.blit(hi_text, (x, y + 25))

def load_high_score():
    try:
        with open("highsocre.txt", "r") as hi_score_file:
            value = hi_score_file.read().strip()
    except FileNotFoundError:
        with open("highsocre.txt", "w") as hi_score_file:
            hi_score_file.write("0")
        value = "0"

    if value == "":
        return 0
    return int(value)

def save_high_score(value):
    with open("highsocre.txt", "w") as hi_score_file:
        hi_score_file.write(str(value))

high_score = load_high_score()

class cars:

    def __init__(self, cars_x, cars_y, cars_image, name):
        self.cars_x = cars_x
        self.cars_y = cars_y
        self.cars_image = cars_image
        self.name = name

    def make_cars(self):
        cars = pygame.Rect(self.cars_x, self.cars_y, 20, 20)
        cars_png = "car_" + str(self.cars_image)+".png"
        colorcars = pygame.image.load(cars_png).convert_alpha()
        resized_cars = pygame.transform.smoothscale(colorcars, [20,20])
        screen.blit(resized_cars, cars)


def cars_num(pixel):
    cars_loc = round(random.randrange(20, pixel - 20)/20)*20
    return cars_loc



while not quit_game:
    #quit logic
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True
            
    
    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                car_x_change = -5
            elif event.key == pygame.K_RIGHT:
                car_x_change = 5

    car_x += car_x_change
    
    cars1 = cars(cars_num(screen_x),cars_num(screen_y), 3, "Green Car")
    cars2 = cars(cars_num(screen_x),cars_num(screen_y), 4, "Blue Car")
    cars3 = cars(cars_num(screen_x),cars_num(screen_y), 4, "Orange Car")
    cars4 = cars(cars_num(screen_x),cars_num(screen_y), 5, "Purple Car")
    cars5 = cars(cars_num(screen_x),cars_num(screen_y), 6, "Sky Car")
    cars_list = [cars1, cars2,cars3,cars4,cars5]

    #Bondries
    if car_x >= (screen_x -90):
            car_x = screen_x - 90
            car_x_change = 0 

    if car_x < 0:
        car_x = 0
        car_x_change = 0
    
    #background and Score Gen
    screen.fill(gray)
    show_score(textx, texty)
    for items in cars_list:
            cars.make_cars(items)
            

    #Players Car Makeing
    car = pygame.Rect(car_x, car_y, car_h, car_w)
    carimage = pygame.image.load("car_1.png").convert_alpha()
    resized_car = pygame.transform.smoothscale(carimage, [car_h, car_w])
    screen.blit(resized_car, car)
    pygame.display.update()

pygame.quit()
quit()