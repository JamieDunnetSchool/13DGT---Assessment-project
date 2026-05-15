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

def message(msg, txt_colour, bkgd_colour):
    txt = font.render(msg, True, txt_colour, bkgd_colour)
    text_box = txt.get_rect(center=(500, 360))
    screen.blit(txt, text_box)

def show_score(x, y):
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    hi_text = font.render("High: " + str(high_score), True, (255, 255, 255))
    screen.blit(score_text, (x, y))
    screen.blit(hi_text, (x, y + 55))

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

class cactus:
    def __init__(self, cactus_x, cactus_y, name, w, h, speed, points):
        self.cactus_x = cactus_x
        self.cactus_y = cactus_y
        self.name = name
        self.w = w
        self.h = h
        self.speed = speed
        self.points = points

    def make_food(self):
        cactu = pygame.Rect(self.cactus_x, self.cactus_y, self.w, self.h)
        cac = pygame.image.load("cactus.png").convert_alpha()
        resized_cac = pygame.transform.smoothscale(cac, [self.w, self.h])
        screen.blit(resized_cac, cactu)

    def hit(self, llama_x, llama_y, llama_w, llama_h):
        global game_ending, final_score, score
        self.cactus_x -= self.speed
        cactus_rect = pygame.Rect(self.cactus_x, self.cactus_y, self.w, self.h)
        llama_rect = pygame.Rect(llama_x, llama_y, llama_w, llama_h)

        if llama_rect.colliderect(cactus_rect):
            if game_ending == False:
                final_score = int(time.time() - start_time) + pass_score
                score = final_score
            game_ending = True

        if self.cactus_x < -self.w:
            self.cactus_x = 1000 + random.randint(200, 600)
            return self.points
        return 0

def reset_game():
    global llama_x, llama_y, llama_y_change, touch_ground, jump_lock
    global score, pass_score, start_time, game_ending, final_score
    global cactus1, cactus2, cactus3, cactus_list

    llama_x = 100
    llama_y = 220
    llama_y_change = 0
    touch_ground = False
    jump_lock = False

    score = 0
    pass_score = 0
    final_score = 0
    start_time = time.time()
    game_ending = False

    cactus1 = cactus(1200, cactus_y, "cactus1", cactus_w, cactus_h, 10, 1)
    cactus2 = cactus(1600, cactus_y, "cactus2", cactus_w, cactus_h, 10, 1)
    cactus3 = cactus(2000, cactus_y, "cactus3", cactus_w, cactus_h, 10, 1)
    cactus_list = [cactus1, cactus2, cactus3]

cactus1 = cactus(1200, cactus_y, "cactus1", cactus_w, cactus_h, 10, 1)
cactus2 = cactus(1600, cactus_y, "cactus2", cactus_w, cactus_h, 10, 1)
cactus3 = cactus(2000, cactus_y, "cactus3", cactus_w, cactus_h, 10, 1)
cactus_list = [cactus1, cactus2, cactus3]
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
    
    if car_x >= (screen_x -90):
            car_x = screen_x - 90
            car_x_change = 0 

    if car_x < 0:
        car_x = 0
        car_x_change = 0
    
    #background and Score Gen
    screen.fill(gray)
    show_score(textx, texty)

    #Car Makeing
    car = pygame.Rect(car_x, car_y, car_h, car_w)
    carimage = pygame.image.load("car_1.png").convert_alpha()
    resized_car = pygame.transform.smoothscale(carimage, [car_h, car_w])
    screen.blit(resized_car, car)
    pygame.display.update()

    


pygame.quit()
quit()