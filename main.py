########################################################################################################################
#                       KARL, SOPHIA & AMANDA - EKSAMENSPROJEKT I PROGRAMMERING B 2024                                 #
########################################################################################################################

# Import libraries/frameworks
import math
import random
import pygame
from pygame import mixer
from Classes import Tile
from Classes import Player
from Classes import Wall
from Classes import Button
from Classes import Item

# Initializing frameworks/libraries
pygame.init()
mixer.init()

# Set frames per second
fps = 69
timer = pygame.time.Clock()

# Key variables - Player 1
wKey = pygame.K_w
sKey = pygame.K_s
aKey = pygame.K_a
dKey = pygame.K_d

# Key variables - Player 2
upKey = pygame.K_UP
leftKey = pygame.K_LEFT
rightKey = pygame.K_RIGHT
downKey = pygame.K_DOWN

# Speed variables for the players
player1moveSpeed = 3
player2moveSpeed = 3

# Tile and wall width variables
tileW = 60
wallW = 20

# Set up game window
screenWidth, screenHeight = pygame.display.Info().current_h, pygame.display.Info().current_h
canvasWidth, canvasHeight = 1980, 1980  # Spillets størrelse
menuWidth, menuHeight = 700, 700    # Menuernes størrelse
gameWindow = pygame.display.set_mode([screenWidth - screenHeight / 5, screenHeight - screenHeight / 5])
surface = pygame.Surface((canvasWidth, canvasHeight))
pygame.display.set_caption('aMAZEing')  # Sætter spillets navn

# Define center coordinates
centerX, centerY = canvasWidth / 2, canvasHeight / 2
centerButtonX, centerButtonY = 700 / 2, 700 / 2

# Important global variables
level = 0
startH = 80
spacing = tileW + wallW

# Tile list
tiles = []
floorTiles = []

# Wall lists
outerWalls = []
innerWalls = []

# Game status variables

Running = True
StartMenu = True
PauseMenu = False

# Loading background image and scaling it
backgroundImg = pygame.image.load("Sprites/BackgroundStartMenu.png").convert_alpha()
backgroundImg = pygame.transform.scale(backgroundImg, (screenWidth - screenHeight / 5, screenHeight - screenHeight / 5))

# Loading button images
startButtonImg = pygame.image.load("Sprites/StartButton.png").convert_alpha()
rulesButtonImg = pygame.image.load("Sprites/Rules Button.png").convert_alpha()
exitButtonImg = pygame.image.load("Sprites/Exit.png").convert_alpha()
resumeButtonImg = pygame.image.load("Sprites/ResumeButton.png").convert_alpha()

# Button instances
startButton = Button(gameWindow, centerButtonX, 280, startButtonImg, 1.5)
rulesButton = Button(gameWindow, centerButtonX, 390, rulesButtonImg, 1.5)
exitButton = Button(gameWindow, centerButtonX, 500, exitButtonImg, 1.5)
exitButtonPauseMenu = Button(gameWindow, centerButtonX, 410, exitButtonImg, 1.5)
resumeButton = Button(gameWindow, centerButtonX, 300, resumeButtonImg, 1.5)

# Generate maze function
def newLevel():
    global level, countdown, player1, player2

    tiles.clear()
    outerWalls.clear()
    innerWalls.clear()

    level += 1

    findDimensions()
    placeFloor()
    placeTiles()
    placeOuterWalls()
    placeInnerWalls()

    countdown = math.ceil(mazeW/2) * mazeH + 5
    #(countdown)

    # Player instances
    player1 = Player(surface, centerX - math.floor(mazeW/2) * spacing - wallW/2, mazeH * spacing + wallW, 20, 20, "orchid1", 1)
    player2 = Player(surface,  centerX + math.floor(mazeW/2) * spacing - wallW/2, mazeH * spacing + wallW, 20, 20, "olivedrab1", 2)

    players = [player1, player2]


# FindDimensions function
def findDimensions():
    global mazeW, mazeH

    mazeW = random.randrange(2 + level, 5 + level)
    mazeH = random.randrange(2 + level, 5 + level)
    #print(mazeW)
    #print(mazeH)

    if mazeW % 2 == 0 or mazeH % 2 == 0:
        print('error!')
        findDimensions()


# Floor function
def placeFloor():

    for i in range(mazeH * math.ceil(mazeW / 2)):
        if i % math.ceil(mazeW/2) == 0:
            floorM = Tile(surface, centerX - tileW/2 - wallW, startH + spacing * math.floor(i/math.ceil(mazeW/2)) - wallW,
                            tileW + 2 * wallW, tileW + 2 * wallW, "darkslategray", i)
            floorTiles.append(floorM)
        else:
            floorH = Tile(surface,
                            centerX - tileW/2 + spacing * (i - math.floor(i / math.ceil(mazeW/2)) * math.ceil(mazeW/2)) - wallW,
                            startH + spacing * math.floor(i/math.ceil(mazeW/2)) - wallW, tileW + 2 * wallW, tileW + 2 * wallW, 'darkslategray', i)
            floorTiles.append(floorH)

            floorV = Tile(surface,
                            centerX - tileW/2 - spacing * (i - math.floor(i / math.ceil(mazeW / 2)) * math.ceil(mazeW / 2)) - wallW,
                            startH + spacing * math.floor(i / math.ceil(mazeW / 2)) - wallW, tileW + 2 * wallW, tileW + 2 * wallW, 'darkslategray', i)
            floorTiles.append(floorV)


# Place tiles function
def placeTiles():
    for i in range(mazeH * math.ceil(mazeW / 2)):
        if i % math.ceil(mazeW/2) == 0:
            peñoslgM = Tile(surface, centerX - tileW/2, startH + spacing * math.floor(i/math.ceil(mazeW/2)),
                            tileW, tileW, "darkslategray4", i)
            tiles.append(peñoslgM)
        else:
            peñoslgH = Tile(surface,
                            centerX - tileW/2 + spacing * (i - math.floor(i / math.ceil(mazeW/2)) * math.ceil(mazeW/2)),
                            startH + spacing * math.floor(i/math.ceil(mazeW/2)), tileW, tileW, 'darkslategray4', i)
            tiles.append(peñoslgH)

            peñoslgV = Tile(surface,
                            centerX - tileW/2 - spacing * (i - math.floor(i / math.ceil(mazeW / 2)) * math.ceil(mazeW / 2)),
                            startH + spacing * math.floor(i / math.ceil(mazeW / 2)), tileW, tileW, 'darkslategray4', i)
            tiles.append(peñoslgV)


# Place outer walls function
def placeOuterWalls():
    leftWall = Wall(surface, centerX + tileW/2 - spacing * math.floor((mazeW + 2)/2),
                   startH - wallW, wallW, mazeH * spacing + wallW, "darkslategray2")
    rightWall = Wall(surface, centerX - tileW / 2 - wallW + spacing * math.floor((mazeW + 2) / 2),
                    startH - wallW, wallW, mazeH * spacing + wallW, "darkslategray2")

    leftUpperWall = Wall(surface, centerX + tileW/2 - spacing * math.floor((mazeW + 2)/2),
                   startH - wallW, math.floor(mazeW/2) * spacing + wallW, wallW, "darkslategray2")
    rightUpperWall = Wall(surface, centerX + tileW/2,
                   startH - wallW, math.floor(mazeW/2) * spacing + wallW, wallW, "darkslategray2")

    bottomWall = Wall(surface, centerX + tileW/2 - spacing * math.floor((mazeW + 2)/2),
                   startH + mazeH * spacing - wallW, mazeW * spacing + wallW, wallW, "darkslategray2")

    outerWalls.append(leftWall)
    outerWalls.append(rightWall)
    outerWalls.append(leftUpperWall)
    outerWalls.append(rightUpperWall)
    outerWalls.append(bottomWall)

# Place inner walls function
def placeInnerWalls():
    randomizing = True

    #for i in range(1):
    for i in range((mazeW - 1) * (mazeH - 1)):
        xPos = centerX + tileW / 2 - spacing * math.floor(mazeW / 2) + spacing * (
                    i - math.floor(i / (mazeW - 1)) * (mazeW - 1))
        yPos = startH + tileW + spacing * math.floor(i / (mazeW - 1))

        iterations = random.randrange(1) # 1, 3
        oppositeDirection = None

        for j in range(iterations):
            wallW, wallH = 20, 20

            while randomizing:
                direction = random.randrange(1, 5)
                if direction != oppositeDirection:
                    break

            #print(direction)

            if direction == 1:
                wallH = 5 * wallW
                yPos -= 4 * wallW
                oppositeDirection = 2

            elif direction == 2:
                wallH = 5 * wallW
                oppositeDirection = 1

            elif direction == 3:
                wallW = 5 * wallH
                xPos -= 4 * wallH
                oppositeDirection = 4

            elif direction == 4:
                wallW = 5 * wallH
                oppositeDirection = 3

            sùlñpèg = Wall(surface, xPos, yPos, wallW, wallH, 'darkslategray2')

            innerWalls.append(sùlñpèg)

            if direction == 2:
                yPos += 4 * wallW

            elif direction == 4:
                xPos += 4 * wallH

                                #############################
                                ### START PÅ RANDOM POINT ###
                                #############################

# https://www.geeksforgeeks.org/python-ways-to-shuffle-a-list/

def checkEscape():
    global player1, player2

    if player1.y < 60: #tilpas evt.
        player1.escaped = True

    if player2.y < 60:  # tilpas evt.
        player2.escaped = True

    if player1.escaped == True and player2.escaped == True:
        newLevel()

newLevel()

# Things happening while startmenu is equal to true
while StartMenu:
    for event in pygame.event.get():
        # Check for keys pressed
        if event.type == pygame.KEYDOWN:
            # Close game if escape key is pressed
            if event.key == pygame.K_ESCAPE:
                StartMenu = False
                Running = False
                PauseMenu = False
            elif event.key == pygame.K_SPACE:
                StartMenu = False
        # Close game if the game windows close button is pressed
        elif event.type == pygame.QUIT:
            StartMenu = False
            Running = False

    gameWindow.blit(backgroundImg, (0, 0))

    if startButton.draw():
        print("Klikket på start!!!")
        StartMenu = False

    if rulesButton.draw():
        print("Klikket på rules!!!")

    if exitButton.draw():
        print("Klikket på exit!!!")
        StartMenu = False
        Running = False

    pygame.display.flip()


# Things happening while running is equal to true
while Running:
    playMousePos = pygame.mouse.get_pos()

    # Backgroundcolor for the game
    surface.fill('black')

    timer.tick(fps)

    pygame.draw.rect(surface, 'black', pygame.Rect(0, 0, canvasWidth, canvasHeight), 60)

    for floor in floorTiles:
        floor.draw()

    for tile in tiles:
        tile.draw()

    for wall in outerWalls:
        wall.draw()

    for wall in innerWalls:
        wall.draw()

    #draw exit graphics
    pygame.draw.rect(surface, 'yellow', pygame.Rect(centerX - 3 * wallW / 2, startH - wallW, wallW * 3, wallW))

    if not player1.escaped:
        player1.move(wKey, sKey, aKey, dKey, player1moveSpeed)
        player1.draw()

    if not player2.escaped:
        player2.move(upKey, downKey, leftKey, rightKey, player2moveSpeed)
        player2.draw()

    for object in outerWalls:
        player1.checkCollision(object)
        player2.checkCollision(object)

    for object in innerWalls:
        player1.checkCollision(object)
        player2.checkCollision(object)

    for object in floorTiles:
        player1.checkDeath(object)
        player2.checkDeath(object)

    if player2.collide:
        print('death')

    countdown -= 0.01 + 0.005 * level

    for i in range(2):
        for tile in tiles:
            if tile.count >= countdown:
                tiles.remove(tile)

        for floor in floorTiles:
            if floor.count >= countdown:
                floorTiles.remove(floor)

    checkEscape()

    # Check for pygame events
    for event in pygame.event.get():

        # Check for keys pressed
        if event.type == pygame.KEYDOWN:
            # Close game if escape key is pressed
            if event.key == pygame.K_ESCAPE:
                Running = False
                PauseMenu = True

            if event.key == pygame.K_SPACE:
                newLevel()

        # Close game if the game windows close button is pressed
        elif event.type == pygame.QUIT:
            Running = False

    # Mark Moment
    gameWindow.blit(pygame.transform.scale(surface, (screenHeight - screenHeight / 5, screenHeight - screenHeight / 5)), (0, 0))
    pygame.display.flip()

    # Things happening while pausemenu is equal to true
    while PauseMenu:
        for event in pygame.event.get():
            # Check for keys pressed
            if event.type == pygame.KEYDOWN:
                # Close game if escape key is pressed
                if event.key == pygame.K_ESCAPE:
                    StartMenu = False
                    Running = True
                    PauseMenu = False
                # elif event.key == pygame.K_SPACE:
                # StartMenu = False
            # Close game if the game windows close button is pressed
            elif event.type == pygame.QUIT:
                StartMenu = False
                Running = True
                PauseMenu = False

        gameWindow.fill((10, 10, 10))

        if resumeButton.draw():
            print("Klikket resume!!!")
            Running = True
            PauseMenu = False

        if exitButtonPauseMenu.draw():
            print("Klikket exit!!!")
            PauseMenu = False

        pygame.display.flip()



'''
               XXXXXXXXX
         XXXXXXXXXXXXXXXXXXXXX
      XXXXXX   XXXXXXXXX   XXXXXX
      XXXXXX   XXXXXXXXX   XXXXXX
      XXXXXXXXXXXXXXXXXXXXXXXXXXX
      XXX   XXXXXXXXXXXXXXX   XXX
      XXXXXX   XXXXXXXXX   XXXXXX
         XXXXXX         XXXXXX
               XXXXXXXXX
'''
