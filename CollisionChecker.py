from main import *
from Classes import *

# Hjælp af Mark :)
def collisionChecker(self, player1, player2):
    if player1.x + player1.width > player2.x and player1.x < player2.x + player2.width and player1.y + player1.height \
            > player2.y and player1.y < player2.y + player2.height:
        return True
    return False
