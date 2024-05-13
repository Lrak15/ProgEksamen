import math
import pygame

pygame.init()

# Game Object parent class
class GameObject:
    def __init__(self, game_window, xPos, yPos, width, height, color):
        self.gw = game_window
        self.x = xPos
        self.y = yPos
        self.w = width
        self.h = height
        self.color = color

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

        if up_moved and left_moved != 0:
            up_moved = -math.sin(math.radians(45)) * movespeed
            left_moved = -math.sin(math.radians(45)) * movespeed

        if up_moved and right_moved != 0:
            up_moved = -math.sin(math.radians(45)) * movespeed
            right_moved = math.sin(math.radians(45)) * movespeed

        if down_moved and left_moved != 0:
            down_moved = math.sin(math.radians(45)) * movespeed
            left_moved = -math.sin(math.radians(45)) * movespeed

        if down_moved and right_moved != 0:
            down_moved = math.sin(math.radians(45)) * movespeed
            right_moved = math.sin(math.radians(45)) * movespeed

        self.x += left_moved + right_moved
        self.y += up_moved + down_moved


class Button:
    def __init__(self, x, y, image, scaling):
        width = image.get_width()
        height = image.get_height()
        self.image = image.transform.scale(image, (int(width * scaling), int(height * scaling)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def drawButton(self):
        surface.blit(self, (self.rect.x, self.rect.y))



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
