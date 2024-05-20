# Import af libraries
import math
import pygame

# Initialisering af Pygame
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
        self.hitbox = pygame.Rect(self.x, self.y, self.w, self.h)   # Laver en hitbox ud fra spillerens dimensioner

    # Metode der tegner spilleren i form af en rektangel
    def draw(self):
        pygame.draw.rect(self.gw, self.color, pygame.Rect(self.x, self.y, self.w, self.h))


# Player klassen
class Player(GameObject):
    def __init__(self, game_window, xPos, yPos, width, height, color, player):
        super().__init__(game_window, xPos, yPos, width, height, color)
        self.player = player
        self.topCollide = False
        self.bottomCollide = False
        self.leftCollide = False
        self.rightCollide = False
        self.escaped = False
        self.OnTile = False
        self.direction = None
        self.destroying = False
        self.destroyHitbox = pygame.Rect(self.x, self.y, self.w, self.h)
        self.destroytime = 100

    # Metode der tjekker om spillere kolliderer med et objekt
    def checkCollision(self, object):
        self.hitbox = pygame.Rect(self.x, self.y, self.w, self.h)
        collisionTolerance = 10
        # Forskellige kollisionsscenarier
        if self.hitbox.colliderect(object.hitbox):
            if abs(self.hitbox.top - object.hitbox.bottom) < collisionTolerance:
                self.topCollide = True
            elif abs(self.hitbox.bottom - object.hitbox.top) < collisionTolerance:
                self.bottomCollide = True
            if abs(self.hitbox.left - object.hitbox.right) < collisionTolerance:
                self.leftCollide = True
            elif abs(self.hitbox.right - object.hitbox.left) < collisionTolerance:
                self.rightCollide = True

    # Metode der tjekker om spilleren er død
    def checkDeath(self, object):
        if self.hitbox.colliderect(object.hitbox):
            self.OnTile = True

    # Metode der tillader spilleren at kunne bevæge sig
    def move(self, up, down, left, right, movespeed):
        up_moved = 0
        down_moved = 0
        left_moved = 0
        right_moved = 0
        key = pygame.key.get_pressed()

        if not self.destroying:
            if key[up] and not self.topCollide:
                up_moved = -movespeed
            if key[down] and not self.bottomCollide:
                down_moved = movespeed
            if key[left] and not self.leftCollide:
                left_moved = -movespeed
            if key[right] and not self.rightCollide:
                right_moved = movespeed

        # Spilleren kan bevæge sig skråt vha. sinus
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

        self.topCollide, self.bottomCollide, self.leftCollide, self.rightCollide = False, False, False, False

    def findDirection(self, up, down, left, right):
        key = pygame.key.get_pressed()

        if key[left]:
            self.direction = "left"
        if key[right]:
            self.direction = "right"
        if key[up]:
            self.direction = "up"
        if key[down]:
            self.direction = "down"

        print(self.direction)

        if self.direction == "up":
            self.destroyHitbox = pygame.Rect(self.x, self.y - self.h, self.w, self.h)
        if self.direction == "down":
            self.destroyHitbox = pygame.Rect(self.x, self.y + self.h, self.w, self.h)
        if self.direction == "left":
            self.destroyHitbox = pygame.Rect(self.x - self.w, self.y, self.w, self.h)
        if self.direction == "right":
            self.destroyHitbox = pygame.Rect(self.x + self.w, self.y, self.w, self.h)


# Tile klassen
class Tile(GameObject):
    def __init__(self, game_window, xPos, yPos, width, height, color, count):
        super().__init__(game_window, xPos, yPos, width, height, color)
        self.count = count  # Indikere antallet af tiles


# Wall klassen
class Wall(GameObject):
    def __init__(self, game_window, xPos, yPos, width, height, color):
        super().__init__(game_window, xPos, yPos, width, height, color)
        self.hitbox = pygame.Rect(self.x, self.y, self.w, self.h)


# Fog klassen (ikke en del af MVP'en)
#class Fog(GameObject):
    #def __init__(self, game_window, xPos, yPos, width, height, color):
        #super().__init__(game_window, xPos, yPos, width, height, color)


# Item klassen
class Item(GameObject):
    def __init__(self, game_window, xPos, yPos, width, height, color, name):
        super().__init__(game_window, xPos, yPos, width, height, color)
        self.name = name    # Navn på item

# Button klassen
class Button:   # (credit: Coding With Russ YT)
    def __init__(self, game_window, centerX, centerY, image, scale):
        self.gw = game_window
        width = image.get_width()       # Får billedets bredde
        height = image.get_height()     # Får billedets højde
        scaled_width = int(width * scale)       # Scaler bredden på billedet
        scaled_height = int(height * scale)     # Scaler højden på billedet
        self.image = pygame.transform.scale(image, (scaled_width, scaled_height))   # Scaler hele billedet
        # Laver en rect ud fra billedet størrelse, og sætter dets anchor point til centrum
        self.rect = self.image.get_rect(center=(centerX, centerY))
        self.clicked = False    # Knapperne er ALDRIG klikket på til at starte på

    # Metode der tegner knapperne
    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()

        # Tjekker om spilleren trykker på knappen, mens pilen er derpå
        if self.rect.collidepoint(pos):
            # Hvis der trykkes på knappen
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True
        # Hvis der ikke trykkes på knappen
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # Tegner rent faktisk knappen på skærmen
        self.gw.blit(self.image, self.rect)

        return action