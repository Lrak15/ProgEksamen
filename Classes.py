import pygame

from main import *

# Game Object parent class
class GameObject:
    def __init__(self, x, y, width, height, game_window, object):
        self.gw = game_window
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        self.image = pygame.image.load(object)
        self.rect = self.image.get_rect()

    def draw(self):
        gameWindow.blit(self.image, (self.x, self.y))


# Meget simpel player klasse for nu, ændres senere, men fin til debugging atm :))
class Player(GameObject):
    def __init__(self, width, height, xPos, yPos, player):
        self.x = xPos
        self.y = yPos
        self.w = width
        self.h = height
        self.player = player


# Tile klassen
class Tile(GameObject):
    def __init__(self,  count):
        self.count =


        # Jeg er meget sikker, jeg går ikke til medierne


# TODO: Wall class


# TODO: Fog class


# TODO: Enemy class
