import pygame
import math
import random

# Initialize Pygame and Font
pygame.init()
pygame.font.init()
font1 = pygame.font.Font("./Text.ttf", 40)
font2 = pygame.font.Font("./Text.ttf", 20)
font3 = pygame.font.Font("./Text.ttf", 30)

# Importing Image Files
cloud = pygame.image.load("Clouds.png")
grass = pygame.image.load("Grass.png")
pipe = pygame.image.load("pipe.png")
pipe1 = pygame.image.load("pipe1.png")
clappy = pygame.image.load("ClappyBird.png")
space = pygame.image.load("SpaceBackground.jpg")

# Import Sounds
flapSound = pygame.mixer.Sound("FlapSound.ogg")
deathSound = pygame.mixer.Sound("DeathSound.ogg")

# Set Screen
size = (500, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Clappy Bird")

# Define Colours and Clock
clock = pygame.time.Clock()
blue = (50, 175, 255)
yellow = (200, 200, 50)
gray = (125, 125, 125)
lightBrown = (242, 202, 152)
brown = (229, 176, 110)
white = (255, 255, 255)
black = (0, 0, 0)

gravity, yspeed = 0.8, 0

tickRate = 100

# Jump Mechanic Variables
framesSinceJump = 0
framesSinceFall = 0
isJumping = False
firstJump = False

# Grass and Pipe Coordinates
x1 = 1200
x1mid = 1500
x2 = 1800
x2mid = 2100

# Pipe Gap Size and Different Sizes
pipeDifference = 765 #575
heights = [430]

# Pipe Heights
h1 = random.choice(heights)
h2 = random.choice(heights)
h3 = random.choice(heights)
h4 = random.choice(heights)

score = 0

# High Score
myFile = open("highscore.txt", "r")
highscore = int(myFile.readline())
myFile.close()

isPlaying = False

level1 = False
level2 = False
levelSelect = False
mainRun = True
deathRun = True


# Jump
def jump_distance1(x):
    return int(6 * math.log((1/7*x+2), 2))

def add_score():
    global score
    score += 1
# Bird Position
x, y = 240, 630

# Grass and Pipe Coordinates Must be Reset
x1 = 1200
x1mid = 1500
x2 = 1800
x2mid = 2100

canJump = True

level1 = True
while level1:
    # Event Manager
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            level2 = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not isJumping and canJump:
                isJumping = True
                firstJump = True
                framesSinceJump = 0
                yspeed = 0
                canJump = False
                flapSound.play()

    # Jumping
    if isJumping:
        y = y - jump_distance1(framesSinceJump)

        framesSinceJump += tickRate

        if framesSinceJump > 800:
            isJumping = False
            yspeed = 0

    # Gravity
    else:
        if framesSinceFall > 300 and firstJump:
            yspeed += gravity
            y += yspeed
            framesSinceFall = 0

        framesSinceFall += tickRate

    # Game Boundaries
    if y < 0:
        y = 15
    if y >= 600:
        y = 600
        canJump = True
        

    x1 -= 2
    x1mid -= 2
    x2 -= 2
    x2mid -= 2

    # Make Pipes Move
    if x1 + 600 < 0:
        x1 = x2 + 600
        h1 = random.choice(heights)
        x1mid = x1 + 300
        h2 = random.choice(heights)
    if x2 + 600 < 0:
        x2 = x1 + 600
        h3 = random.choice(heights)
        x2mid = x2 + 300
        h4 = random.choice(heights)

    # Give player time before game starts
    if not isPlaying:
        if x1 < 300:
            isPlaying = True
            isFirst = True
            add_score()
    elif isFirst and x == x1mid:
        isFirst = False
        add_score()
    elif x == x1 or x == x1mid or x == x2 or x == x2mid:
        add_score()

    # Pipe hitboxes
    hitboxes = [
                pygame.Rect(x1, h1, 90, 600),
                pygame.Rect(x1, h1 - pipeDifference, 90, 600),
                pygame.Rect(x1mid, h2, 90, 600),
                pygame.Rect(x1mid, h2 - pipeDifference, 90, 600),
                pygame.Rect(x2, h3, 90, 600),
                pygame.Rect(x2, h3 - pipeDifference, 90, 600),
                pygame.Rect(x2mid, h4, 90, 600),
                pygame.Rect(x2mid, h4 - pipeDifference, 90, 600)
                ]
                          
    screen.blit(space, pygame.rect.Rect(0,0,500,700))
    # Flappy Bird
    bird = pygame.Rect(x, y, 20, 20)
    screen.blit(clappy, pygame.rect.Rect(x-10, y-3, 20, 20))

    # Draw the pipes
    for i in range(0, len(hitboxes), 2):
        screen.blit(pipe, hitboxes[i])
        screen.blit(pipe1, hitboxes[i + 1])

    # Display Current Score
    screen.blit(font2.render("Score:" + str(score), False, (255, 255, 255)), (10, 10))

    # Collision Detection
    for i in range(0, len(hitboxes)):
        if bird.colliderect(hitboxes[i]):
            level2 = False
            deathSound.play()
            break

    pygame.display.flip()
    clock.tick(tickRate)

pygame.quit()

