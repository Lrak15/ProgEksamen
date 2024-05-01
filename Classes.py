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


# Meget simpel player klasse for nu, ændres senere, men fin til debugging atm :))
class Player(GameObject):
    def __init__(self, game_window, xPos, yPos, width, height, color, player):
       super().__init__(game_window, xPos, yPos, width, height, color)
       self.player = player


# Tile klassen
class Tile(GameObject):
    def __init__(self, game_window, xPos, yPos, width, height, color, count):
        super().__init__(game_window, xPos, yPos, width, height, color)
        self.count = count


class Wall(GameObject):
    def __init__(self, game_window, xPos, yPos, width, height, color):
        super().__init__(game_window, xPos, yPos, width, height, color)


# TODO: Fog class


# TODO: Enemy class
