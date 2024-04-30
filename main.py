# TODO: Basic setup and screen

# Import libraries
import math
from random import randrange

import pygame
from pygame import mixer

pygame.init()
mixer.init()

# Set frames per second
fps = 9999999999999999999999999999999999999999999999999999999999999999999999999999999996999999999
timer = pygame.time.Clock()

# Set up game window
screenWidth, screenHeight = pygame.display.Info().current_w, pygame.display.Info().current_w
gameWindow = pygame.display.set_mode([screenWidth, screenHeight])
pygame.display.set_caption('aMAZEing')

# Define center coordinates
centerX, centerY = screenWidth / 2, screenWidth / 2
print(screenWidth)
print(centerX)
print(screenHeight)
print(centerY)

# Define pixel size
# Format for new pixel size should be 320:180
px = round(screenHeight / 180)

Running = True

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

while Running:
    timer.tick(fps)

    movementSpeed = 1
    w_moved = 0
    a_moved = 0
    s_moved = 0
    d_moved = 0

    gameWindow.fill('purple')

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


