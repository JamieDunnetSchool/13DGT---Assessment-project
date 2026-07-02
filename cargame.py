"""this program is a llama game for playing."""

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
black = (0, 0, 0)
gray = (140, 140, 140)
white = (255, 255, 255)
green = (34, 191, 37)

quit_game = False
start_page = True
game_ending = False
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

# Speed variable
speed = random.randint(3, 5)

# Text create


def message(msg, txt_colour, bkgd_colour, x_coward, y_corward):
    """Return the color and font values of the text."""
    txt = font.render(msg, True, txt_colour, bkgd_colour)
    text_box = txt.get_rect(center=(x_coward, y_corward))
    screen.blit(txt, text_box)

# Score Create


def show_score(x, y):
    """Return the lattuide and landutude values of the text."""
    score_text = font.render("Score: " + str(score), True, black)
    hi_text = font.render("High: " + str(high_score), True, black)
    screen.blit(score_text, (x, y))
    screen.blit(hi_text, (x, y + 25))

# Import high score


def load_high_score():
    """Return this highscore to this file."""
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
    """Return this saves the high score back to the file."""
    with open("highsocre.txt", "w") as hi_score_file:
        hi_score_file.write(str(value))


high_score = load_high_score()
# NPC car creating


class Cars:
    """Represents the NPC cars the player dogdes."""

    def __init__(self, cars_x, cars_y, cars_image, name, speed):
        """Initialise objects."""
        self.cars_x = cars_x
        self.cars_y = cars_y
        self.cars_image = cars_image
        self.name = name
        self.speed = speed

    def make_cars(self):
        """Generate Cars."""
        cars_rect = pygame.Rect(self.cars_x, self.cars_y, cars_h, cars_w)
        cars_png = "car_" + str(self.cars_image) + ".png"
        colorcars = pygame.image.load(cars_png).convert_alpha()
        resized_cars = pygame.transform.smoothscale(colorcars,
                                                    [cars_h, cars_w])
        pipe_flip = pygame.transform.flip(resized_cars, False, True)
        screen.blit(pipe_flip, cars_rect)

    def move(self):
        """Initialise objects to move."""
        self.cars_y += self.speed

    def collision(self, player_rect):
        """Initialise Collisions with players car."""
        npc_rect = pygame.Rect(self.cars_x + 8, self.cars_y + 8, cars_h - 16,
                               cars_w - 16)
        return player_rect.colliderect(npc_rect)


def safe_spawn_lane(current_car, new_y):
    """Initialise Cars in doable spots."""
    blocked_lanes = []

    for other in cars_list:
        if other != current_car:
            if other.cars_x in lanes:
                blocked_lanes.append(other.cars_x)

    free_lanes = [lane for lane in lanes if lane not in blocked_lanes]

    # Only allow 3 lanes full at once
    if len(free_lanes) <= 1:
        return -500

    if len(free_lanes) > 0:
        return random.choice(free_lanes)

    return -500


random.shuffle(lanes)

cars1 = Cars(lanes[0], random.randint(-300, -100), 2, "Green Car", speed)
cars2 = Cars(lanes[1], random.randint(-700, -500), 3, "Blue Car", speed)
cars3 = Cars(lanes[2], random.randint(-1100, -900), 4, "Orange Car", speed)
cars4 = Cars(-500, random.randint(-1500, -1300), 5, "Purple Car", speed)
cars5 = Cars(-500, random.randint(-1900, -1700), 6, "Sky Car", speed)
cars_list = [cars1, cars2, cars3, cars4, cars5]


def reset_game():
    """Return the game start when death occurces."""
    global car_x, car_y, car_y_change
    global score, pass_score, game_ending, final_score
    global cars1, cars2, cars3, cars4, cars5, cars_list
    global speed

    car_x = 300
    car_y = 650
    car_y_change = 0

    random.shuffle(lanes)

    speed = random.randint(3, 5)

    cars1 = Cars(lanes[0], random.randint(-300, -100), 2, "Green Car", speed)
    cars2 = Cars(lanes[1], random.randint(-700, -500), 3, "Blue Car", speed)
    cars3 = Cars(lanes[2], random.randint(-1100, -900), 4, "Orange Car", speed)
    cars4 = Cars(-500, random.randint(-1500, -1300), 5, "Purple Car", speed)
    cars5 = Cars(-500, random.randint(-1900, -1700), 6, "Sky Car", speed)
    cars_list = [cars1, cars2, cars3, cars4, cars5]

    score = 0
    pass_score = 0
    final_score = 0

    game_ending = False


# Gameloop
while not quit_game:

    while start_page is True:

        screen.fill(gray)

        ground_rect = pygame.Rect(0, 750, screen_y, screen_x)
        pygame.draw.rect(screen, green, ground_rect)

        message("Car Vroom Game", gray, white, 375, 300)
        message("Press SPACE to start", gray, white, 375, 360)
        message("Use LEFT and RIGHT arrows to move", gray, white, 375, 420)
        message("Press X to quit", gray, white, 375, 480)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game = True
                start_page = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start_page = False
                    reset_game()
                if event.key == pygame.K_x:
                    quit_game = True
                    start_page = False
                    break

    while game_ending is True:

        if score > high_score:
            high_score = score
            save_high_score(high_score)

        screen.fill(gray)
        ground_rect = pygame.Rect(0, 750, screen_y, screen_x)
        pygame.draw.rect(screen, green, ground_rect)
        show_score(textx, texty)
        message("You died! Press X to quit, C to play again", gray, white, 375,
                400)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game = True
                game_ending = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    quit_game = True
                    game_ending = False
                    break
                elif event.key == pygame.K_c:
                    reset_game()
                    continue

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True

    keys = pygame.key.get_pressed()
    car_x_change = 0

    if keys[pygame.K_LEFT]:
        car_x_change = -5

    if keys[pygame.K_RIGHT]:
        car_x_change = 5

    car_x += car_x_change

    screen.fill(gray)

    # Bondries
    if car_x >= 670 - 90:
        car_x = 670 - 90

    if car_x < 80:
        car_x = 80

    car = pygame.Rect(car_x + 8, car_y + 8, car_h - 16, car_w - 16)

    for items in cars_list:
        items.make_cars()
        items.move()

        if items.collision(car):
            game_ending = True

        if items.cars_y > screen_y:
            items.cars_y = random.randint(-800, -300)

            speed = random.randint(3, 5)
            items.speed = speed

            items.cars_x = safe_spawn_lane(items, items.cars_y)
            items.cars_image = random.randint(2, 6)

            score += 1

    # Draws lines above screen
    ground_rect = pygame.Rect(lane1_x, 800 - line_size_h, line_size_w,
                              line_size_h)
    pygame.draw.rect(screen, white, ground_rect)

    ground_rect = pygame.Rect(lane2_x, 800 - line_size_h, line_size_w,
                              line_size_h)
    pygame.draw.rect(screen, white, ground_rect)

    ground_rect = pygame.Rect(lane3_x, 800 - line_size_h, line_size_w,
                              line_size_h)
    pygame.draw.rect(screen, white, ground_rect)

    ground_rect = pygame.Rect(80, 800 - line_size_h, line_size_w, line_size_h)
    pygame.draw.rect(screen, white, ground_rect)

    ground_rect = pygame.Rect(670, 800 - line_size_h, line_size_w, line_size_h)
    pygame.draw.rect(screen, white, ground_rect)

    # Green Green Grass
    ground_rect = pygame.Rect(0, 800 - line_size_h, 80, 2000)
    pygame.draw.rect(screen, green, ground_rect)

    ground_rect = pygame.Rect(680, 800 - line_size_h, 80, 2000)
    pygame.draw.rect(screen, green, ground_rect)

    show_score(textx, texty)

    # Players Car Making
    carimage = pygame.image.load("car_1.png").convert_alpha()
    resized_car = pygame.transform.smoothscale(carimage, [car_h, car_w])
    player_car = pygame.Rect(car_x, car_y, car_h, car_w)
    screen.blit(resized_car, player_car)

    # Write new high score I achived.
    if score > high_score:
        high_score = score
    save_high_score(high_score)

    pygame.display.update()

pygame.quit()
quit()
