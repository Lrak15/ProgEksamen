#_______________________________________________________________________________________________________________________
#                       KARL, SOPHIA & AMANDA - EKSAMENSPROJEKT I PROGRAMMERING B 2024
#_______________________________________________________________________________________________________________________

# Import libraries/frameworks
import math
import random
# from random import randrange
import pygame
from pygame import mixer
from Classes import Tile
from Classes import Player
from Classes import Wall
# from Classes import Button

# Initializing frameworks/libraries
pygame.init()
mixer.init()

# Program status variable
Running = True

# Set frames per second
fps = 20
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

tileW = 60
wallW = 20

boots = 1
pickaxe = 2
mask = 3
dagger = 4

# items = [boots, pickaxe, mask, dagger]
# player1items, player2items = [], []

#for item in items:
#    lilbro = (items[item], False)
#    player1items.append(lilbro)
#    player2items.append(lilbro)


# Set up game window
screenWidth, screenHeight = pygame.display.Info().current_h, pygame.display.Info().current_h
canvasWidth, canvasHeight = 1980, 1980
gameWindow = pygame.display.set_mode([screenWidth, screenHeight])
surface = pygame.Surface((canvasWidth, canvasHeight))
pygame.display.set_caption('aMAZEing')

# Define center coordinates
centerX, centerY = canvasWidth / 2, canvasHeight / 2

# INSTANCES
#_______________________________________________________________________________________________________________________

level = 0


def generateMaze():
    global level, countdown

    level += 1

    tiles.clear()
    outerWalls.clear()
    innerWalls.clear()

    findDimensions()
    placeTiles(mazeW, mazeH)
    placeOuterWalls(mazeW, mazeH)
    placeInnerWalls(mazeW, mazeH)

    countdown = 100


def findDimensions():
    global mazeW, mazeH
    mazeW = random.randrange(3, 23)
    mazeH = random.randrange(3, 23)
    print(mazeW)
    print(mazeH)
    if mazeW % 2 == 0 or mazeH % 2 == 0:
        print('error!')
        findDimensions()



startH = 80

spacing = tileW + wallW

# TODONE: Liste med tiles

# Tiles instance
tiles = []

def placeTiles(mazeW, mazeH):
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


# Player instances
player1 = Player(surface, 20, 20, 20, 20, "blue", 1)
player2 = Player(surface, 50, 50, 20, 20, "red", 2)



# TODONE : Create outer walls from Wall class

outerWalls = []
def placeOuterWalls(mazeW, mazeH):
    leftWall = Wall(surface, centerX + tileW/2 - spacing * math.floor((mazeW + 2)/2),
                   startH - wallW, wallW, mazeH * spacing + wallW, "magenta")
    rightWall = Wall(surface, centerX - tileW / 2 - wallW + spacing * math.floor((mazeW + 2) / 2),
                    startH - wallW, wallW, mazeH * spacing + wallW, "magenta")

    leftUpperWall = Wall(surface, centerX + tileW/2 - spacing * math.floor((mazeW + 2)/2),
                   startH - wallW, math.floor(mazeW/2) * spacing + wallW, wallW, "magenta")
    rightUpperWall = Wall(surface, centerX + tileW/2,
                   startH - wallW, math.floor(mazeW/2) * spacing + wallW, wallW, "magenta")

    bottomWall = Wall(surface, centerX + tileW/2 - spacing * math.floor((mazeW + 2)/2),
                   startH + mazeH * spacing - wallW, mazeW * spacing + wallW, wallW, "magenta")

    outerWalls.append(leftWall)
    outerWalls.append(rightWall)
    outerWalls.append(leftUpperWall)
    outerWalls.append(rightUpperWall)
    outerWalls.append(bottomWall)



# TODO : Create walls from Wall class

# Wall instance
innerWalls = []

def placeInnerWalls(mazeW, mazeH):
    randomizing = True

    #for i in range(1):
    for i in range((mazeW - 1) * (mazeH - 1)):

        xPos = centerX + tileW / 2 - spacing * math.floor(mazeW / 2) + spacing * (
                    i - math.floor(i / (mazeW - 1)) * (mazeW - 1))
        yPos = startH + tileW + spacing * math.floor(i / (mazeW - 1))

        iterations = random.randrange(1, 5)

        oppositeDirection = None

        for j in range(iterations):

            wallW, wallH = 20, 20

            while randomizing:
                direction = random.randrange(1, 5)
                if direction != oppositeDirection:
                    break

            print(direction)

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

            sùlñpèg = Wall(surface, xPos, yPos, wallW, wallH, (310 - 63 * iterations, 63 * iterations, 0))
            innerWalls.append(sùlñpèg)

            if direction == 2:
                yPos += 4 * wallW

            elif direction == 4:
                xPos += 4 * wallH

#############################
### START PÅ RANDOM POINT ###
#############################

# https://www.geeksforgeeks.org/python-ways-to-shuffle-a-list/


'''
    for i in range((mazeW - 1) * (mazeH - 1)):
        sùlñpèg = Wall(surface, centerX + tileW/2 - spacing * math.floor(mazeW/2) + spacing * (i - math.floor(i/(mazeW - 1)) * (mazeW - 1)),
                       startH + tileW + spacing * math.floor(i/(mazeW - 1)), wallW, wallW, "magenta")
        innerWalls.append(sùlñpèg)
        num = random.randrange(3)
        if num > 1:
            sùlñpèg2 = Wall(surface, centerX + tileW / 2 - spacing * math.floor(mazeW / 2) + spacing * (
                        i - math.floor(i / (mazeW - 1)) * (mazeW - 1)),
                           startH + tileW + spacing * math.floor(i / (mazeW - 1)), wallW, wallW * 4, "magenta")
            innerWalls.append(sùlñpèg2)
'''





'''
# Load sounds
# Inspiration from:
# https://stackoverflow.com/questions/65247656/how-do-i-change-the-volume-of-the-sound-or-music-in-pygame

shootSound = pygame.mixer.Sound("Sfx/shootsound.mp3")
shootSound.set_volume(0.2)

music = 'Sfx/Amynedd Main Theme SMT-2 0.8S.mp3'
pygame.mixer.music.load(music)

# mixer.music.load("")
mixer.music.set_volume(0.2)


def check_collisions(structure, player):
    global w_moved, a_moved, s_moved, d_moved
    collision_tolerance = 10 * px
    if structure.hitbox.colliderect(player.hitbox):
        print('collision')
        if abs(player.hitbox.top - structure.hitbox.bottom) < collision_tolerance:
            w_moved = 0
        if abs(player.hitbox.left - structure.hitbox.right) < collision_tolerance:
            a_moved = 0
        if abs(player.hitbox.bottom - structure.hitbox.top) < collision_tolerance:
            s_moved = 0
        if abs(player.hitbox.right - structure.hitbox.left) < collision_tolerance:
            d_moved = 0


# Playing music that repeats 69 times
# Inspiration from:
# https://stackoverflow.com/questions/35068209/how-do-i-repeat-music-using-pygame-mixer
pygame.mixer.music.play(69)
'''


'''
findDimensions()

placeTiles(mazeW, mazeH)
placeOuterWalls(mazeW, mazeH)
placeInnerWalls(mazeW, mazeH)
'''

generateMaze()

# ON THE WINDOW
#_______________________________________________________________________________________________________________________
running = True

while running:
    playMousePos = pygame.mouse.get_pos()

    # Backgroundcolor for the game
    surface.fill('darkslategrey')

    timer.tick(fps)

    # Speed variables for the players
    player1moveSpeed = 10
    player2moveSpeed = 10

    pygame.draw.rect(surface, 'black', pygame.Rect(0, 0, canvasWidth, canvasHeight),60)

    # BLITTING INSTANCES
    # __________________________________________________________________________________________________________________

    for tile in tiles:
        tile.draw()

    for wall in outerWalls:
        wall.draw()

    for wall in innerWalls:
        wall.draw()

    # player1.move(wKey, aKey, sKey, dKey)
    player1.move(wKey, sKey, aKey, dKey, player1moveSpeed)
    player2.move(upKey, downKey, leftKey, rightKey, player2moveSpeed)

    player1.draw()
    player2.draw()

    # print(countdown)

    countdown -= 0.1 * level

    for i in range(2):
        for tile in tiles:
            if tile.count >= countdown:
                tiles.remove(tile)

    # Check for pygame events
    for event in pygame.event.get():

        # Check for keys pressed
        if event.type == pygame.KEYDOWN:
            # Close game if escape key is pressed
            if event.key == pygame.K_ESCAPE:
                running = False

            if event.key == pygame.K_SPACE:
                generateMaze()

        # Close game if the game windows close button is pressed
        elif event.type == pygame.QUIT:
            running = False

        # Update game window

        # Mark Moment
        gameWindow.blit(pygame.transform.scale(surface, (screenHeight, screenHeight)), (0, 0))
        pygame.display.flip()




















# TODO: Main loop










'''
               XXXXXXXXX
         XXXXXXXXXXXXXXXXXXXXX
      XXXXXX   XXXXXXXXX   XXXXXX
      XXXXXX   XXXXXXXXX   XXXXXX
      XXXXXXXXXXXX   XXXXXXXXXXXX
      XXX   XXXXXXXXXXXXXXX   XXX
      XXXXXX   XXXXXXXXX   XXXXXX
         XXXXXX         XXXXXX
               XXXXXXXXX
'''


