"""this program is a llama game for playing"""

# Imports
import pygame
import random

# Screen Size and Screen Create
pygame.init()
screen_x = 750
screen_y = 800
screen = pygame.display.set_mode((screen_x, screen_y))

# Icon and Caption
pygame.display.set_caption("Car Vroom game")
game_icon = pygame.image.load("game_icon.png")
pygame.display.set_icon(game_icon)

# Colors
gray = (140, 140, 140)
white = (255, 255, 255)

quit_game = False
score = 0
high_score = 0
textx = 10
texty = 10
font = pygame.font.Font("freesansbold.ttf", 20)

# Players car variables
car_x = 300
car_y = 650
car_h = 95 
car_w = 150
car_x_change = 0
car_y_change = 0

# NPC car variables
cars_y = 0
cars_x = 0
cars_w = 150 
cars_h = 95
cars_y_change = 0

# Line and road variables
line_size_h = 2000
line_size_w = 10
lane1_x = 225
lane2_x = 375
lane3_x = 525
lanes = [110, 260, 410, 560]

# Text create
def message(msg, txt_colour, bkgd_colour):
    """Return the color and font values of the text."""
    txt = font.render(msg , True, txt_colour, bkgd_colour)
    text_box = txt.get_rect(center=(144, 256))
    screen.blit(txt, text_box)

# Score Create
def show_score(x, y):
    """Return the lattuide and landutude values of the text."""
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    hi_text = font.render("High: " + str(high_score), True, (255, 255, 255))
    screen.blit(score_text, (x, y))
    screen.blit(hi_text, (x, y + 25))

# Import high score
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

# Export highscore
def save_high_score(value):
    with open("highsocre.txt", "w") as hi_score_file:
        hi_score_file.write(str(value))

high_score = load_high_score()

# NPC car creating
class cars:

    def __init__(self, cars_x, cars_y, cars_image, name, speed):
        self.cars_x = cars_x
        self.cars_y = cars_y
        self.cars_image = cars_image
        self.name = name
        self.speed = speed

    def make_cars(self):
        cars_rect = pygame.Rect(self.cars_x, self.cars_y, 0, 0)
        cars_png = "car_" + str(self.cars_image)+".png"
        colorcars = pygame.image.load(cars_png).convert_alpha()
        resized_cars = pygame.transform.smoothscale(colorcars, [cars_w, cars_h])
        pipe_flip = pygame.transform.flip(resized_cars, False, True)
        screen.blit(pipe_flip, cars_rect)

    def move(self):
        self.cars_y += self.speed
        print(f"{self.name} is at {self.cars_y}")
    
    def collision(self, player_rect):
        return player_rect.colliderect(
            pygame.Rect(self.cars_x, self.cars_y, cars_w, cars_h)
        )

#def cars_num(pixel):
    #cars_loc = round(random.randrange(20, pixel - 20))
    #return cars_loc

cars1 = cars(random.choice(lanes), random.randint(-800, -100), 2, "Green Car", 10)
cars2 = cars(random.choice(lanes), random.randint(-800, -100), 3, "Blue Car", 10)
cars3 = cars(random.choice(lanes), random.randint(-800, -100), 4, "Orange Car", 10)
cars4 = cars(random.choice(lanes), random.randint(-800, -100), 5, "Purple Car", 10)
cars5 = cars(random.choice(lanes), random.randint(-1200, -900), 6, "Sky Car", 10)
cars_list = [cars1, cars2, cars3, cars4, cars5]

# Gameloop
while not quit_game:
    # quit logic
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True
            
    keys = pygame.key.get_pressed()
    car_x_change = 0
    if keys[pygame.K_LEFT]:
        car_x_change = - 5
        car_y_change = 0
    if keys[pygame.K_RIGHT]:
        car_x_change = 5
        car_y_change = 0

    car_x += car_x_change

    # Bondries
    if car_x >= (screen_x -90):
            car_x = screen_x - 90
            car_x_change = 0 

    if car_x < 0:
        car_x = 0
        car_x_change = 0
    
    # background and Score Gen
    screen.fill(gray)
    show_score(textx, texty)

    car = pygame.Rect(car_x, car_y, car_w, car_h)

    for items in cars_list:
        items.make_cars()
        items.move()

        if items.collision(car):
            quit_game = True

        if items.cars_y > screen_y:
            items.cars_y = random.randint(-600, -150)
            items.cars_x = random.choice(lanes)
            score += 1
        
    # lines
    ground_rect = pygame.Rect(lane1_x,800  - line_size_h, line_size_w, 
                              line_size_h)
    pygame.draw.rect(screen, white, ground_rect)

    ground_rect = pygame.Rect(lane2_x,800  - line_size_h, line_size_w, 
                              line_size_h)
    pygame.draw.rect(screen, white, ground_rect)

    ground_rect = pygame.Rect(lane3_x,800  - line_size_h, line_size_w, 
                              line_size_h)
    pygame.draw.rect(screen, white, ground_rect)

    # Players Car Makeing
    carimage = pygame.image.load("car_1.png").convert_alpha()
    resized_car = pygame.transform.smoothscale(carimage, [car_w, car_h])
    screen.blit(resized_car, car)
    pygame.display.update()

pygame.quit()
quit()