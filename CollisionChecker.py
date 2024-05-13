from main import player1, player2

# Hjælp af Mark :)
def collisionChecker(player1, player2):   # Player1 og Player2 er instances fra main
    if player1.x + player1.width > player2.x and player1.x < player2.x + player2.width and player1.y + player1.height \
            > player2.y and player1.y < player2.y + player2.height:
        return True
    return False
