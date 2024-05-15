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
        self.hitbox = pygame.Rect(self.x, self.y, self.w, self.h)

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

    def checkCollision(self, object):

        self.hitbox = pygame.Rect(self.x, self.y, self.w, self.h)

        self.topCollide, self.bottomCollide, self.leftCollide, self.rightCollide = False, False, False, False

        collisionTolerance = 10

        if self.hitbox.colliderect(object.hitbox):
            print('collision')
            if abs(self.hitbox.top - object.hitbox.bottom) < collisionTolerance:
                self.topCollide = True
                print('top collision')
            elif abs(self.hitbox.bottom - object.hitbox.top) < collisionTolerance:
                self.bottomCollide = True
                print('bottom collision')
            if abs(self.hitbox.left - object.hitbox.right) < collisionTolerance:
                self.leftCollide = True
                print('left collision')
            elif abs(self.hitbox.right - object.hitbox.left) < collisionTolerance:
                self.rightCollide = True
                print('right collision')

    def move(self, up, down, left, right, movespeed):
        up_moved = 0
        down_moved = 0
        left_moved = 0
        right_moved = 0
        key = pygame.key.get_pressed()

        if key[up] and not self.topCollide:
            up_moved = -movespeed
        if key[down] and not self.bottomCollide:
            down_moved = movespeed
        if key[left] and not self.leftCollide:
            left_moved = -movespeed
        if key[right] and not self.rightCollide:
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


# Tile klassen
class Tile(GameObject):
    def __init__(self, game_window, xPos, yPos, width, height, color, count):
        super().__init__(game_window, xPos, yPos, width, height, color)
        self.count = count


# Wall klassen
class Wall(GameObject):
    def __init__(self, game_window, xPos, yPos, width, height, color):
        super().__init__(game_window, xPos, yPos, width, height, color)
        self.hitbox = pygame.Rect(self.x, self.y, self.w, self.h)


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


class Button:  # (credit: Coding With Russ YT)
    def __init__(self, game_window, xPos, yPos, image, scale):
        self.gw = game_window
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect(topleft=(xPos, yPos))
        self.clicked = False

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        self.gw.blit(self.image, self.rect)

        return action
