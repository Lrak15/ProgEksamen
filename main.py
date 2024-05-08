#_______________________________________________________________________________________________________________________
#                       KARL, SOPHIA & AMANDA - EKSAMENSPROJEKT I PROGRAMMERING B 2024
#_______________________________________________________________________________________________________________________

# Import libraries/frameworks
import math
from random import randrange
import pygame
from pygame import mixer
from Classes import Tile
from Classes import Player

# Initializing frameworks/libraries
pygame.init()
mixer.init()

# Program status variable
Running = True

font = pygame.font.SysFont("arialblack", 20)

white = (255, 255, 255)

def blitTextOnScreen(text, font, textColor, x, y):
    image = font.render(text, True, textColor)
    surface.blit(image, (x, y))

# Set frames per second
fps = 20
timer = pygame.time.Clock()

# Setting tilecount and countdown
tileCount = 100
countdown = tileCount + 1

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

items = [boots, pickaxe, mask, dagger]
player1items, player2items = [], []

#for item in items:
#    lilbro = (items[item], False)
#    player1items.append(lilbro)
#    player2items.append(lilbro)


# Set up game window
screenWidth, screenHeight = pygame.display.Info().current_h, pygame.display.Info().current_h
canvasWidth, canvasHeight = 2000, 2000
gameWindow = pygame.display.set_mode([screenWidth, screenHeight])
surface = pygame.Surface((canvasWidth, canvasHeight))
pygame.display.set_caption('aMAZEing')

# Define center coordinates
centerX, centerY = canvasWidth / 2, canvasHeight / 2

# INSTANCES
#_______________________________________________________________________________________________________________________

level = 1

mazeW = 19

startH = 40

spacing = tileW + wallW


# Tiles instance
tiles = []




def placeTiles():
    for i in range(tileCount):
        if i % math.ceil(mazeW/2) == 0:
            peñoslgM = Tile(surface, centerX, startH + spacing * math.floor(i/math.ceil(mazeW/2)),
                            tileW, tileW, "blue", i)
            tiles.append(peñoslgM)

        else:
            peñoslgH = Tile(surface, centerX + spacing * (i - math.floor(i / math.ceil(mazeW/2)) * math.ceil(mazeW/2)),
                            startH + spacing * math.floor(i/math.ceil(mazeW/2)), tileW, tileW, 'blue', i)
            tiles.append(peñoslgH)

            peñoslgV = Tile(surface,
                            centerX - spacing * (i - math.floor(i / math.ceil(mazeW / 2)) * math.ceil(mazeW / 2)),
                            startH + spacing * math.floor(i / math.ceil(mazeW / 2)), tileW, tileW, 'blue', i)
            tiles.append(peñoslgV)


# Player instances
player1 = Player(surface, 20, 20, 20, 20, "black", 1)
player2 = Player(surface, 50, 50, 20, 20, "red", 2)

# Wall instance
walls = []

# TODO : Create walls from Wall class


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

def calculate_movement(movement_speed):
    global w_moved, a_moved, s_moved, d_moved

    key_pressed = pygame.key.get_pressed()

    if key_pressed[pygame.K_w]:
        w_moved = movement_speed

    if key_pressed[pygame.K_a]:
        a_moved = movement_speed

    if key_pressed[pygame.K_s]:
        s_moved = -movement_speed

    if key_pressed[pygame.K_d]:
        d_moved = -movement_speed

    # The following code checks if a movement in the vertical direction and a movement in the horizontal direction
    # both aren't equal to 0, meaning that there is diagonal movement. If so, both movement directions, making up
    # the diagonal movement, is shortened, so that the diagonal movement speed is the same speed as vertical or
    # horizontal movement
    if w_moved and a_moved != 0:
        w_moved = math.sin(45) * movement_speed
        a_moved = math.sin(45) * movement_speed

    if w_moved and d_moved != 0:
        w_moved = math.sin(45) * movement_speed
        d_moved = -math.sin(45) * movement_speed

    if s_moved and a_moved != 0:
        s_moved = -math.sin(45) * movement_speed
        a_moved = math.sin(45) * movement_speed

    if s_moved and d_moved != 0:
        s_moved = -math.sin(45) * movement_speed
        d_moved = -math.sin(45) * movement_speed


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

TitleScreen = True
Running = True


for count in range(33):
    timer.tick(15)
    gameWindow.blit(introImages[count], (0, 0))
    # Update game window
    pygame.display.flip()

while TitleScreen:
    timer.tick(fps)

    Customize_character = False
    Options = False

    gameWindow.blit(titleScreen, (0, 0))

    # Check for pygame events
    for event in pygame.event.get():

        # Check for keys pressed
        if event.type == pygame.KEYDOWN:

            # Close game if escape key is pressed
            if event.key == pygame.K_ESCAPE:
                TitleScreen = False
                # Running = False ##########################################################################

        # Close game if the game windows close button is pressed
        elif event.type == pygame.QUIT:
            TitleScreen = False
            Running = False
# Playing music that repeats 69 times
# Inspiration from:
# https://stackoverflow.com/questions/35068209/how-do-i-repeat-music-using-pygame-mixer
pygame.mixer.music.play(69)
'''

placeTiles()

# ON THE WINDOW
#_______________________________________________________________________________________________________________________
while Running:
    timer.tick(fps)

    # Speed variables for the players
    player1moveSpeed = 10
    player2moveSpeed = 10

    # Backgroundcolor for the game
    surface.fill('pink')

    #blitTextOnScreen("Press SPACE to play", font, white, canvasWidth / 2, canvasHeight / 2)


    # BLITTING INSTANCES
    # __________________________________________________________________________________________________________________

    for tile in tiles:
        tile.draw()

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
                Running = False

        # Close game if the game windows close button is pressed
        elif event.type == pygame.QUIT:
            Running = False

    '''

    calculate_movement(movementSpeed)

    for structure in structureHitboxes:
        check_collisions(structure, player)

    graveyardStructureTing.move(w_moved, a_moved, s_moved, d_moved)
    graveyardStructureTing.draw()

    for image in structures:
        image.move(w_moved, a_moved, s_moved, d_moved)
        image.draw()

    for structure in structureHitboxes:
        structure.move(w_moved, a_moved, s_moved, d_moved)
        structure.update()

    for border in borderHitboxes:
        border.draw()

    player.draw(px)

    for attack in projectiles:
        for monster in enemies:
            player_attack(attack, monster)

        if attack.pierce == 0:
            projectiles.remove(attack)
        attack.move(w_moved, a_moved, s_moved, d_moved)
        attack.travel(centerX)
        despawn_projectile(attack)
        attack.draw()

    for monster in enemies:
        if monster.health <= 0:
            enemies.remove(monster)
            willpowerPoints += 1
            pygame.mixer.Sound.play(killSound)
        enemy_attack(monster, player)
        monster.move(w_moved, a_moved, s_moved, d_moved)
        monster.travel(centerX, centerY)
        despawn_enemy(monster)
        monster.draw(centerX, px)

    # fog(temptationPoints)

    # display_mouse_coordinates()

    gameWindow.blit(HUD, (0, 0))

    level_progression = 10 + willpowerLevel * 5
    willpower_bar(willpowerPoints, willpowerLevel, level_progression)
    if willpowerPoints >= level_progression:
        willpowerLevel += 1
        upgradePoints += 1
        willpowerPoints = 0
        pygame.mixer.Sound.play(levelUpSound)

    temptation_graphics(temptationPoints)

    HUD_graphics(upgradePoints)

    if temptationPoints >= 100:

        enemies.clear()

        setbackTime = pygame.time.get_ticks()
        Setback = True

        while Setback:

            # Check for pygame events
            for event in pygame.event.get():

                # Check for keys pressed
                if event.type == pygame.KEYDOWN:

                    # Close game if escape key is pressed
                    if event.key == pygame.K_ESCAPE:
                        Setback = False
                        Running = False

                    elif event.key == pygame.K_SPACE:
                        Setback = False

                # Close game if the game windows close button is pressed
                elif event.type == pygame.QUIT:
                    Setback = False
                    Running = False

            gameWindow.blit(setbackFrame, (0, 0))
            timeSinceSetback = pygame.time.get_ticks() - setbackTime
            setbackText3 = font4.render('get smoked', True, 'black')
            setbackText = font3.render('get smoked', True, 'red')
            setbackText2 = font3.render('time', True, 'black')
            setbackTimer = font2.render(f'{10000 - timeSinceSetback}', True, 'red')
            gameWindow.blit(setbackText3, (118 * px, 75 * px))
            gameWindow.blit(setbackText, (120 * px, 75 * px))
            gameWindow.blit(setbackText2, (120 * px, 95 * px))
            gameWindow.blit(setbackTimer, (125 * px, 100 * px))

            if timeSinceSetback >= 10000:
                Setback = False

            # Update game window
            pygame.display.flip()

        temptationPoints = 0
        willpowerPoints = 0
        willpowerLevel -= 3
        if willpowerLevel < 0:
            willpowerLevel = 0

    if temptationPoints > 0:
        timeSinceTemptation = pygame.time.get_ticks() - temptationTime
        if timeSinceTemptation > 10000:
            Regenerating = True

    if Regenerating:
        regenParameter = timeSinceTemptation / 1000 - 10
        temptationPoints -= (regenParameter * regenParameter) / 50
        print((regenParameter * regenParameter) / 50)



    if temptationPoints < 0:
        Regenerating = False
        temptationPoints = 0


    graphicsDelay -= 1

    '''

    # Update game window

    # Mark Moment
    gameWindow.blit(pygame.transform.scale(surface, (screenHeight, screenHeight)), (0, 0))
    pygame.display.flip()







# TODO: Liste med tiles















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


