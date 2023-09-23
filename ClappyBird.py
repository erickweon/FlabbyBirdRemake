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

# Jump
def jump_distance(x):
    return int((3 / 2.0) * math.log(x + 1, 2))

# Jump
def jump_distance1(x):
    return int(6 * math.log((1/7*x+2), 2))

def add_score():
    global score
    score += 1

run = True

while run:

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
    pipeDifference = 765
    heights = [215, 420, 575]

    # Pipe Heights
    h1 = random.choice(heights)
    h2 = random.choice(heights)
    h3 = random.choice(heights)
    h4 = random.choice(heights)
    h = 430

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

    while mainRun:
        # Event Manager
        mouseClicked = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainRun = False
                deathRun = False
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseClicked = True

        # Get Mouse Position
        mx, my = pygame.mouse.get_pos()

        # Variables For Enlarging Buttons
        button1Inc = 0
        button2Inc = 0

        # If Mouse is Hovering Over the Buttons, Enlarge It
        if mx >= 67 and mx <= 217 and my >= 400 and my <= 475:
            button1Inc = 2
            # If Right Button is Clicked, Play
            if mouseClicked:
               levelSelect = True
               mainRun = False

        # Enlarge the Buttons
        if mx >= 283 and mx <= 433 and my >= 400 and my <= 475:
            button2Inc = 2
            # If Left Button is Clicked, Quit
            if mouseClicked:
                mainRun = False
                deathRun = False
                run = False

        # Draw Background for Main Screen
        screen.fill(blue)
        screen.blit(cloud, pygame.rect.Rect(20, 40, 128, 128))
        screen.blit(grass, pygame.rect.Rect(0, 630, 50, 700))
        # Draw Buttons
        pygame.draw.rect(screen, white, (67-button1Inc, 400-button1Inc, 150+(2*button1Inc), 75+(2*button1Inc)))
        pygame.draw.rect(screen, black, (67-button1Inc, 400-button1Inc, 150+(2*button1Inc), 75+(2*button1Inc)), 2)
        pygame.draw.rect(screen, white, (283-button2Inc, 400-button2Inc, 150+(2*button2Inc), 75+(2*button2Inc)))
        pygame.draw.rect(screen, black, (283-button2Inc, 400-button2Inc, 150+(2*button2Inc), 75+(2*button2Inc)), 2)
        # Write Fonts
        screen.blit(font1.render("Clappy Bird", False, black), (32, 220))
        screen.blit(font2.render("Play", False, black), (101, 430))
        screen.blit(font2.render("Quit", False, black), (320, 430))
        screen.blit(font2.render("High Score: " + str(highscore), False, black), (105, 500))
        pygame.display.flip()

    # Select Level
    while levelSelect:
        # Event Manager
        mouseClicked = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                levelSelect = False
                deathRun = False
                run = False
                level1 = False
                level2 = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseClicked = True

        mx, my = pygame.mouse.get_pos()

        # Variables for Enlarging Buttons
        b1Inc = 0
        b2Inc = 0

        if mx >= 50 and mx <= 450 and my >= 200 and my <= 300:
            # When Hover Over, Enlarge Button
            b1Inc = 2
            # If Button 1 Is Clicked, Go To Level 1
            if mouseClicked:
                level1 = True
                levelSelect = False
        if mx >= 50 and mx <= 450 and my >= 400 and my <= 500:
            # When Hover Over, Enlarge Button
            b2Inc = 2
            # If Button 2 Is Clicked, Go To Level 2
            if mouseClicked:
                level2 = True
                levelSelect = False

        # Draw Background
        screen.fill(blue)
        screen.blit(cloud, pygame.rect.Rect(20, 40, 128, 128))
        screen.blit(grass, pygame.rect.Rect(0, 630, 50, 700))
        # Draw Buttons
        pygame.draw.rect(screen, white, (50-b1Inc, 200-b1Inc, 400+(2*b1Inc), 100+(2*b1Inc)))
        pygame.draw.rect(screen, black, (48-b1Inc, 198-b1Inc, 403+(2*b1Inc), 103+(2*b1Inc)), 2)
        pygame.draw.rect(screen, white, (50-b2Inc, 400-b2Inc, 400+(2*b2Inc), 100+(2*b2Inc)))
        pygame.draw.rect(screen, black, (48-b2Inc, 398-b2Inc, 403+(2*b2Inc), 103+(2*b2Inc)), 2)
        screen.blit(font1.render("Level 1", False, black), (111, 230))
        screen.blit(font1.render("Level 2", False, black), (111, 430))
        pygame.display.flip()

        # Bird Coordinates
        x, y = 240, 680
        # Grass Coordinates
        x1 = 1200
        x2 = 1800

    gravity, yspeed = 0.75, 0
    canJump = True

    while level1:
        # Event Manager
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                level1 = False
                run = False
                deathRun = False
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
            x1mid = x1 + 300
        if x2 + 600 < 0:
            x2 = x1 + 600
            x2mid = x2 + 300

        # Give player time before game starts
        if x == x1 or x == x1mid or x == x2 or x == x2mid:
            add_score()

        # Pipe hitboxes
        hitboxes = [
            pygame.Rect(x1, h, 90, 600),
            pygame.Rect(x1, h - pipeDifference, 90, 600),
            pygame.Rect(x1mid, h, 90, 600),
            pygame.Rect(x1mid, h - pipeDifference, 90, 600),
            pygame.Rect(x2, h, 90, 600),
            pygame.Rect(x2, h - pipeDifference, 90, 600),
            pygame.Rect(x2mid, h, 90, 600),
            pygame.Rect(x2mid, h - pipeDifference, 90, 600)
        ]

        screen.blit(space, pygame.rect.Rect(0, 0, 500, 700))
        # Flappy Bird
        bird = pygame.Rect(x, y, 20, 20)
        screen.blit(clappy, pygame.rect.Rect(x - 10, y - 3, 20, 20))

        # Draw the pipes
        for i in range(0, len(hitboxes), 2):
            screen.blit(pipe, hitboxes[i])
            screen.blit(pipe1, hitboxes[i + 1])

        # Display Current Score
        screen.blit(font2.render("Score:" + str(score), False, (255, 255, 255)), (10, 10))

        # Collision Detection
        for i in range(0, len(hitboxes)):
            if bird.colliderect(hitboxes[i]):
                level1 = False
                deathSound.play()
                break

        pygame.display.flip()
        clock.tick(tickRate)

    # Bird Position
    x, y = 240, 340

    # Reset Gravity
    gravity, yspeed = 1, 0

    # Level 2 Game Loop
    while level2:
        # Event Manager
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                level2 = False
                run = False
                deathRun = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not isJumping:
                    isJumping = True
                    firstJump = True
                    framesSinceJump = 0
                    yspeed = 0
                    flapSound.play()

        # Jumping
        if isJumping:
            y = y - jump_distance(framesSinceJump)

            framesSinceJump += tickRate

            if framesSinceJump > 800:
                isJumping = False
                yspeed = 0

        # Gravity
        else:
            if framesSinceFall > 200 and firstJump:
                yspeed += gravity
                y += yspeed
                framesSinceFall = 0

            framesSinceFall += tickRate

        # Game Boundaries
        if y < 0:
            y = 15
        if y > 680:
            level2 = False
            deathSound.play()

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

        # Background Colour
        screen.fill(blue)

        # Give player time before game starts
        if not isPlaying:
            screen.blit(grass, pygame.Rect(x1-1200, 630, 50, 700))
            screen.blit(grass, pygame.Rect(x2-1200, 630, 50, 700))
            if x1 < 300:
                isPlaying = True
                isFirst = True
                add_score()
        elif isFirst and x == x1mid:
            isFirst = False
            add_score()
        elif isFirst:
            screen.blit(grass, pygame.Rect(x1 - 1200, 630, 50, 700))
            screen.blit(grass, pygame.Rect(x2 - 1200, 630, 50, 700))
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

        # Draw Background
        screen.blit(cloud, pygame.rect.Rect(20, 40, 128, 128))
        screen.blit(grass, pygame.rect.Rect(x1, 630, 50, 700))
        screen.blit(grass, pygame.rect.Rect(x2, 630, 50, 700))

        # Flappy Bird
        bird = pygame.Rect(x, y, 20, 20)
        screen.blit(clappy, pygame.rect.Rect(x-10, y-3, 20, 20))

        # Draw the pipes
        for i in range(0, len(hitboxes), 2):
            screen.blit(pipe, hitboxes[i])
            screen.blit(pipe1, hitboxes[i + 1])

        # Display Current Score
        screen.blit(font2.render("Score:" + str(score), False, (0, 0, 0)), (10, 10))

        # Collision Detection
        for i in range(0, len(hitboxes)):
            if bird.colliderect(hitboxes[i]):
                level2 = False
                deathSound.play()
                break

        pygame.display.flip()
        clock.tick(tickRate)


    # Set New High Score
    if score > highscore:
        myFile = open("highscore.txt", "w")
        myFile.write(str(score))
        myFile.close()

    # Death Screen
    while deathRun:
        mouseClicked = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                deathRun = False
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseClicked = True

        pygame.draw.rect(screen, white, (100, 150, 300, 400))
        pygame.draw.rect(screen, white, (100, 150, 300, 400))
        pygame.draw.rect(screen, black, (105, 155, 290, 390), 2)
        pygame.draw.rect(screen, white, (107, 157, 288, 388))
        mx, my = pygame.mouse.get_pos()

        # Main Menu Button
        if mx >= 125 and mx <= 375 and my >= 300 and my <= 400:
            # Enlarges When Hovering Over
            pygame.draw.rect(screen, black, (123, 298, 254, 104), 2)
            if mouseClicked:
                deathRun = False
        else:
            pygame.draw.rect(screen, black, (125, 300, 250, 100), 2)

        # Quit Button
        if mx >= 125 and mx <= 375  and my >=420 and my <= 520:
            # Enlarges When Hovering Over
            pygame.draw.rect(screen, black, (123, 418, 254, 104), 2)
            if mouseClicked:
                run = False
                deathRun = False
        else:
            pygame.draw.rect(screen, black, (125, 420, 250, 100), 2)

        screen.blit(font2.render("Main Menu", False, black), (165, 340))
        screen.blit(font2.render("Quit", False, black), (209, 463))

        screen.blit(font2.render("Score:" + str(score), False, black), (172, 215))
        if score > highscore:
            screen.blit(font2.render("New Highscore!", False, black), (114, 250))
        else:
            screen.blit(font2.render("Highscore:" + str(highscore), False, black), (140, 250))

        screen.blit(font3.render("GAME OVER", False, black), (119, 170))
        pygame.display.flip()

pygame.quit()
