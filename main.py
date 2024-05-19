########################################################################################################################
#                                                                                                                      #
#                       KARL, SOPHIA & AMANDA - EKSAMENSPROJEKT I PROGRAMMERING B 2024                                 #
#                                                                                                                      #
########################################################################################################################

# Importering af frameworks og libraries
import math
import random
import pygame
from pygame import mixer
from Classes import Tile
from Classes import Player
from Classes import Wall
from Classes import Button
from Classes import Item

# Initialisering af frameworks/libraries
pygame.init()
mixer.init()

# Sætter en framerate for spillet
fps = 69
timer = pygame.time.Clock()

# Bevægelses variabler - Player 1
wKey = pygame.K_w
sKey = pygame.K_s
aKey = pygame.K_a
dKey = pygame.K_d

# Bevægelses variabler - Player 2
upKey = pygame.K_UP
leftKey = pygame.K_LEFT
rightKey = pygame.K_RIGHT
downKey = pygame.K_DOWN

# Hastighedsvariabler til begge spillere
player1moveSpeed = 3
player2moveSpeed = 3

# Tile og wall bredde variabler
tileW = 60
wallW = 20

# Definere og sætter vinduet op
# Finder skærmens dimensioner
screenWidth, screenHeight = pygame.display.Info().current_h, pygame.display.Info().current_h
canvasWidth, canvasHeight = 1980, 1980  # Spillets størrelse
menuWidth, menuHeight = 700, 700    # Menuernes størrelse
gameWindow = pygame.display.set_mode([screenWidth - screenHeight / 5, screenHeight - screenHeight / 5])
surface = pygame.Surface((canvasWidth, canvasHeight))
pygame.display.set_caption('aMAZEing')  # Sætter spillets navn

# Centerkoordinater
centerX, centerY = canvasWidth / 2, canvasHeight / 2    # Vinduet
centerButtonX, centerButtonY = 700 / 2, 700 / 2     # Knapperne

# Vigtige globale variabler
level = 0
startH = 80
spacing = tileW + wallW

# Tile liste
tiles = []
floorTiles = []

# Wall lister
outerWalls = []
innerWalls = []

# Items liste
items = []

# Spil status variabler
Running = True      # For selve spillet
StartMenu = True    # For startmenuen
PauseMenu = False   # For pausemenuen

# Begge spillers Win variabler sættes til False fra start
Player1Win = False
Player2Win = False

# Font
font = pygame.font.Font('Aero.ttf', 250)

# Tekst til når en spiller vinder
player1WinText = font.render('Player 1 Won', True, 'black')
player2WinText = font.render('Player 2 Won', True, 'black')

# Loader baggrunden og scaler det
backgroundImg = pygame.image.load("Sprites/BackgroundStartMenu.png").convert_alpha()
backgroundImg = pygame.transform.scale(backgroundImg, (screenWidth - screenHeight / 5, screenHeight - screenHeight / 5))

# Loader knappernes billeder
startButtonImg = pygame.image.load("Sprites/StartButton.png").convert_alpha()
rulesButtonImg = pygame.image.load("Sprites/Rules Button.png").convert_alpha()
exitButtonImg = pygame.image.load("Sprites/Exit.png").convert_alpha()
resumeButtonImg = pygame.image.load("Sprites/ResumeButton.png").convert_alpha()

# Knap instances
startButton = Button(gameWindow, centerButtonX, 280, startButtonImg, 1.5)
rulesButton = Button(gameWindow, centerButtonX, 390, rulesButtonImg, 1.5)
exitButton = Button(gameWindow, centerButtonX, 500, exitButtonImg, 1.5)
exitButtonPauseMenu = Button(gameWindow, centerButtonX, 410, exitButtonImg, 1.5)
resumeButton = Button(gameWindow, centerButtonX, 300, resumeButtonImg, 1.5)

# Generer labyrint funktion
def newLevel():
    global level, countdown, player1, player2

    # Fjerner den tidligere labyrint med clear
    tiles.clear()
    floorTiles.clear()
    outerWalls.clear()
    innerWalls.clear()
    items.clear()

    # Sætter level variabler én op
    level += 1

    # Genererer en ny labyrint
    findDimensions()
    placeFloor()
    placeTiles()
    placeOuterWalls()
    placeInnerWalls()

    # Generer items i spillet (som er boots, der booster spillernes hastighed)
    for i in range(level):
        itemX = random.randint(centerX - math.floor(mazeW / 2) * spacing, centerX + math.floor(mazeW / 2) * spacing)
        itemY = random.randint(startH, startH + mazeH * spacing)
        item = Item(surface, itemX, itemY, 15, 15, "red", "boots")
        items.append(item)

    # Countdown for flisernes (tiles) forsvinding
    countdown = math.ceil(mazeW/2) * mazeH + 5

    # Player instances
    player1 = Player(surface, centerX - math.floor(mazeW/2) * spacing - wallW/2,
                     mazeH * spacing + wallW, 20, 20, "orchid1", 1)
    player2 = Player(surface,  centerX + math.floor(mazeW/2) * spacing - wallW/2,
                     mazeH * spacing + wallW, 20, 20, "olivedrab1", 2)

    # Gemmer spillerne i en liste
    players = [player1, player2]

# Find dimensioner funktion
def findDimensions():
    global mazeW, mazeH

    mazeW = 3 + random.randrange(level)
    mazeH = 3 + random.randrange(level)

    #print(mazeW)
    #print(mazeH)

    # Sikre at labyrinten ALTID har en ulige bredde og højde
    if mazeW % 2 == 0 or mazeH % 2 == 0 or mazeW > 23 or mazeH > 23:
        print('error!')
        findDimensions()


# Gulv funktion
def placeFloor():
    # Placerer gulvet i labyrinten
    for i in range(mazeH * math.ceil(mazeW / 2)):
        # Laver en midte af gulv til labyrinten
        if i % math.ceil(mazeW/2) == 0:
            floorM = Tile(surface, centerX - tileW/2 - wallW, startH + spacing * math.floor(i/math.ceil(mazeW/2))
                          - wallW, tileW + 2 * wallW, tileW + 2 * wallW, "darkslategray", i)
            floorTiles.append(floorM)
        # Laver gulvet til højre
        else:
            floorH = Tile(surface,
                          centerX - tileW/2 + spacing * (i - math.floor(i / math.ceil(mazeW/2)) * math.ceil(mazeW/2))
                          - wallW, startH + spacing * math.floor(i/math.ceil(mazeW/2)) - wallW, tileW + 2 * wallW, tileW
                          + 2 * wallW, "darkslategray", i)
            floorTiles.append(floorH)
        # Laver gulvet til venstre
            floorV = Tile(surface, centerX - tileW/2 - spacing * (i - math.floor(i / math.ceil(mazeW / 2)) *
                          math.ceil(mazeW / 2)) - wallW, startH + spacing * math.floor(i / math.ceil(mazeW / 2)) -
                          wallW, tileW + 2 * wallW, tileW + 2 * wallW, "darkslategray", i)
            floorTiles.append(floorV)


# Placér fliser funktion
def placeTiles():
    # Placerer fliserne i labyrinten
    for i in range(mazeH * math.ceil(mazeW / 2)):
        # Laver en midte af fliser i labyrinten
        if i % math.ceil(mazeW/2) == 0:
            tilesM = Tile(surface, centerX - tileW/2, startH + spacing * math.floor(i/math.ceil(mazeW/2)),
                          tileW, tileW, "darkslategray4", i)
            tiles.append(tilesM)
        else:
            # Laver fliserne til højre
            tilesH = Tile(surface, centerX - tileW/2 + spacing * (i - math.floor(i / math.ceil(mazeW/2)) *
                          math.ceil(mazeW/2)), startH + spacing * math.floor(i/math.ceil(mazeW/2)), tileW, tileW,
                          "darkslategray4", i)
            tiles.append(tilesH)
            # laver fliserne til venstre
            tilesV = Tile(surface, centerX - tileW/2 - spacing * (i - math.floor(i / math.ceil(mazeW / 2)) *
                          math.ceil(mazeW / 2)), startH + spacing * math.floor(i / math.ceil(mazeW / 2)), tileW,
                          tileW, "darkslategray4", i)
            tiles.append(tilesV)


# Placér de yderste vægge funktion
def placeOuterWalls():
    # Instances til væggene i labyrinten
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

# Placér indvendige vægge funktion
def placeInnerWalls():
    randomizing = True

    #for i in range(1):
    for i in range((mazeW - 1) * (mazeH - 1)):
        xPos = centerX + tileW / 2 - spacing * math.floor(mazeW / 2) + spacing * (
                    i - math.floor(i / (mazeW - 1)) * (mazeW - 1))
        yPos = startH + tileW + spacing * math.floor(i / (mazeW - 1))

        iterations = random.randrange(1, 3)
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


# Funktion der tjekker om spillerne er ude af labyrinten og har fundet udgangen
def checkEscape():
    global player1, player2

    # Sammenligner udgangen koordinater med begge af spillernes
    if player1.y < 60:
        player1.escaped = True
    if player2.y < 60:
        player2.escaped = True
    # Først når begge er ude af labyrinten genereres der en ny labyrint
    if player1.escaped == True and player2.escaped == True:
        newLevel()

# Funktion der tjekker om spillerne har vundet
def checkWin():
    global Player1Win, Player2Win

    player1.OnTile = False
    player2.OnTile = False

    # Tjekker om spillerne er på fliserne ellers dør de
    for object in floorTiles:
        player1.checkDeath(object)
        player2.checkDeath(object)

    if not player1.OnTile:
        Player2Win = True

    if not player2.OnTile:
        Player1Win = True

newLevel()

# Mens StartMenu er lig med True
while StartMenu:
    for event in pygame.event.get():
        # Tjekker om spilleren trykker på en tast
        if event.type == pygame.KEYDOWN:
            # Lukker spillet hvis de trykker på ESC
            if event.key == pygame.K_ESCAPE:
                StartMenu = False
                Running = False
                PauseMenu = False
            # Starter spillet hvis de trykker på SPACE
            elif event.key == pygame.K_SPACE:
                StartMenu = False
        # Lukker spillet hvis den røde knap i venstre-øvre hjørne trykkes
        elif event.type == pygame.QUIT:
            StartMenu = False
            Running = False

    # Blitter baggrundsbilledet
    gameWindow.blit(backgroundImg, (0, 0))

    # Når knapperne trykkes
    # Når start knappen trykkes på starter spillet
    if startButton.draw():
        print("Klikket på start!!!")
        StartMenu = False
    # Når rules knappen trykkes kan man se spillet regler (IKKE IMPLEMENTERET)
    if rulesButton.draw():
        print("Klikket på rules!!!")
    # Når exit knappen trykkes lukkes spillet
    if exitButton.draw():
        print("Klikket på exit!!!")
        StartMenu = False
        Running = False

    pygame.display.flip()


# Når Running er lig med True
while Running:
    global players
    playMousePos = pygame.mouse.get_pos()

    # Baggrundsfarve til spillet
    surface.fill('black')

    timer.tick(fps)

    pygame.draw.rect(surface, 'black', pygame.Rect(0, 0, canvasWidth, canvasHeight), 60)

    # Tegner gulvet
    for floor in floorTiles:
        floor.draw()

    # Tegner fliserne
    for tile in tiles:
        tile.draw()

    # Tegner væggene
    for wall in outerWalls:
        wall.draw()

    # Tegner de indvendige vægge
    for wall in innerWalls:
        wall.draw()

    # Tegner items'ne i spillet
    for item in items:
        if player1.hitbox.colliderect(item.hitbox):
            player1moveSpeed += 0.5
            print("SPEEDYYYY 1")
            items.remove(item)
        if player2.hitbox.colliderect(item.hitbox):
            player2moveSpeed += 0.5
            print("SPEDDDDYYY 2")
            items.remove(item)
        item.draw()

    # Tegner udgangens grafik
    pygame.draw.rect(surface, 'yellow', pygame.Rect(centerX - 3 * wallW / 2, startH - wallW, wallW * 3, wallW))

    if player1.OnTile and not player1.escaped:
        player1.move(wKey, sKey, aKey, dKey, player1moveSpeed)
        player1.findDirection(wKey, sKey, aKey, dKey)
        player1.draw()

    if player1.destroying:
        player1.destroytime -= 1
        if player1.destroytime > 50:
            pygame.draw.rect(surface, (255, 5.1 * player1.destroytime, 0), player1.destroyHitbox)
        else:
            pygame.draw.rect(surface, (2.55 * player1.destroytime, 255 - 2.55 * player1.destroytime, 0),
                             player1.destroyHitbox)

    if player1.destroytime == 0:
        player1.destroying = False
        player1.destroytime = 100

        for wall in innerWalls:
            if player1.destroyHitbox.colliderect(wall.hitbox):
                innerWalls.remove(wall)

    if player2.OnTile and not player2.escaped:
        player2.move(upKey, downKey, leftKey, rightKey, player2moveSpeed)
        player2.findDirection(upKey, downKey, leftKey, rightKey)
        player2.draw()

    if player2.destroying:
        player2.destroytime -= 1
        pygame.draw.rect(surface, (2.55 * player2.destroytime, 255, 0), player2.destroyHitbox)

    if player2.destroytime == 0:
        player2.destroying = False
        player2.destroytime = 100

        for wall in innerWalls:
            if player2.destroyHitbox.colliderect(wall.hitbox):
                innerWalls.remove(wall)

    # Tjekker for kollision mellem spillerne og væggene
    for object in outerWalls:
        player1.checkCollision(object)
        player2.checkCollision(object)

    # Tjekker for kollision mellem spillerne og de indvendige vægge
    for object in innerWalls:
        player1.checkCollision(object)
        player2.checkCollision(object)

    # Fliserne forsvinder hurtigere jo højere level man er i
    countdown -= 0.01 + 0.005 * level

    # Placere fliserne
    for i in range(2):
        for tile in tiles:
            # Fjerner fliser
            if tile.count >= countdown:
                tiles.remove(tile)

        # Fjerner gulvet
        for floor in floorTiles:
            if floor.count >= countdown:
                floorTiles.remove(floor)

    checkWin()
    checkEscape()

    for event in pygame.event.get():
        # Tjekker om der trykkes på nogle taster
        if event.type == pygame.KEYDOWN:
            # Tjekker om der trykkes på nogle taster
            if event.key == pygame.K_ESCAPE:
                Running = False
                PauseMenu = True
            # Trykker man SPACE øges level og der genereres en ny labyrint
            if event.key == pygame.K_SPACE:
                newLevel()
            if event.key == pygame.K_e:
                player1.destroying = True
            if event.key == pygame.K_l:
                player2.destroying = True
        # Lukker spillet hvis den røde knap i venstre-øvre hjørne trykkes
        elif event.type == pygame.QUIT:
            Running = False

    print(player1.destroytime)
    print(player2.destroytime)

    # Mark Moment
    gameWindow.blit(pygame.transform.scale(surface, (screenHeight - screenHeight / 5,
                    screenHeight - screenHeight / 5)), (0, 0))
    pygame.display.flip()

    # Når Player1Win er lig med True
    while Player1Win:
        # Blitter at spiller 1 vandt på skærmen
        pygame.draw.rect(surface, 'orchid1', pygame.Rect(centerX - canvasWidth/2.2, centerY - canvasWidth/10,
                         canvasWidth / 1.1, canvasHeight/5))
        surface.blit(player1WinText, (180, 900))

        gameWindow.blit(pygame.transform.scale(surface, (screenHeight - screenHeight / 5,
                                               screenHeight - screenHeight / 5)), (0, 0))
        pygame.display.flip()

        for event in pygame.event.get():
            # Check for keys pressed
            if event.type == pygame.KEYDOWN:
                # Close game if escape key is pressed
                if event.key == pygame.K_ESCAPE:
                    Running = False
                    Player1Win = False
            # Close game if the game windows close button is pressed
            elif event.type == pygame.QUIT:
                Running = False
                Player1Win = False

    # Mens Player2Win er lig med True
    while Player2Win:
        # Blitter at spiller 2 har vundet på skærmen
        pygame.draw.rect(surface, 'olivedrab1', pygame.Rect(centerX - canvasWidth / 2.2,
                        centerY - canvasWidth / 10, canvasWidth / 1.1, canvasHeight / 5))
        surface.blit(player2WinText, (150, 900))

        gameWindow.blit(pygame.transform.scale(surface, (screenHeight - screenHeight / 5,
                                                screenHeight - screenHeight / 5)), (0, 0))
        pygame.display.flip()

        for event in pygame.event.get():
            # Check for keys pressed
            if event.type == pygame.KEYDOWN:
                # Close game if escape key is pressed
                if event.key == pygame.K_ESCAPE:
                    Running = False
                    Player2Win = False
            # Close game if the game windows close button is pressed
            elif event.type == pygame.QUIT:
                Running = False
                Player2Win = False

    # Når PauseMenu er lig med True
    while PauseMenu:
        for event in pygame.event.get():
            # Tjekker om der trykkes på nogle taster
            if event.type == pygame.KEYDOWN:
                # Trykkes der ESC så starter spillet igen
                if event.key == pygame.K_ESCAPE:
                    StartMenu = False
                    Running = True
                    PauseMenu = False
                # elif event.key == pygame.K_SPACE:
                # StartMenu = False
            # Lukker spillet hvis den røde knap i venstre-øvre hjørne trykkes
            elif event.type == pygame.QUIT:
                StartMenu = False
                Running = True
                PauseMenu = False

        # Sætter en baggrundsfarve til pausemenuen
        gameWindow.fill((10, 10, 10))

        # Tegner "fortsæt-knappen"
        if resumeButton.draw():
            print("Klikket resume!!!")
            # Trykkes den starter spillet igen
            Running = True
            PauseMenu = False

        # Tegner "forlad-knappen"
        if exitButtonPauseMenu.draw():
            print("Klikket exit!!!")
            # Lukker hele spillet
            PauseMenu = False

        pygame.display.flip()


'''
               XXXXXXXXX
         XXXXXXXXXXXXXXXXXXXXX
      XXXXXX   XXXXXXXXX   XXXXXX
      XXXXXX   XXXXXXXXX   XXXXXX
      XXXXXXXXXXXXXXXXXXXXXXXXXXX
      XXXXXXXXXXXXXXXXXXXXXXXXXXX
      XXX   XXXXXXXXXXXXXXX   XXX
      XXXXXX   XXXXXXXXX   XXXXXX
         XXXXXX         XXXXXX
               XXXXXXXXX
'''