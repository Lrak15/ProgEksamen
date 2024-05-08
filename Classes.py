import math

import pygame

# Game Object parent class
class GameObject:
    def __init__(self, game_window, xPos, yPos, width, height, color):

        self.gw = game_window
        self.x = xPos
        self.y = yPos
        self.w = width
        self.h = height
        self.color = color
        self.px = round(pygame.display.Info().current_h/180)

    def draw(self):
        pygame.draw.rect(self.gw, self.color, pygame.Rect(self.x, self.y, self.w, self.h))


# Player klassen
class Player(GameObject):
    def __init__(self, game_window, xPos, yPos, width, height, color, player):
       super().__init__(game_window, xPos, yPos, width, height, color)

       self.player = player

    def move(self, up, down, left, right, movespeed):
        up_moved = 0
        down_moved = 0
        left_moved = 0
        right_moved = 0
        key = pygame.key.get_pressed()

        if key[up]:
            up_moved = -movespeed
        if key[down]:
            down_moved = movespeed
        if key[left]:
            left_moved = -movespeed
        if key[right]:
            right_moved = movespeed

        '''The following code checks if a movement in the vertical direction and a movement in the horizontal direction
        both aren't equal to 0, meaning that there is diagonal movement. If so, both movement directions, making up
        the diagonal movement, is shortened, so that the diagonal movement speed is the same speed as vertical or
        horizontal movement'''

        if up_moved and left_moved != 0:
            up_moved = -math.sin(45) * movespeed
            left_moved = -math.sin(45) * movespeed

        if up_moved and right_moved != 0:
            up_moved = -math.sin(45) * movespeed
            right_moved = math.sin(45) * movespeed

        if down_moved and left_moved != 0:
            down_moved = math.sin(45) * movespeed
            left_moved = -math.sin(45) * movespeed

        if down_moved and right_moved != 0:
            down_moved = math.sin(45) * movespeed
            right_moved = math.sin(45) * movespeed

        # Movement in all directions is added up
        self.x += left_moved + right_moved
        self. y += up_moved + down_moved


# Tile klassen
class Tile(GameObject):
    def __init__(self, game_window, xPos, yPos, width, height, color, count):
        super().__init__(game_window, xPos, yPos, width, height, color)
        self.count = count


# Wall klassen
class Wall(GameObject):
    def __init__(self, game_window, xPos, yPos, width, height, color):
        super().__init__(game_window, xPos, yPos, width, height, color)


# Fog klassen
class Fog(GameObject):
    def __init__(self, game_window, xPos, yPos, width, height, color):
        super().__init__(game_window, xPos, yPos, width, height, color)


# Item klassen
class Item(GameObject):
    def __init__(self, game_window, xPos, yPos, width, height, color, name, pickedUp):
        super().__init__(game_window, xPos, yPos, width, height, color)

        self.name = name
        self.picked = pickedUp

