from board import Board



#Initialize board
tictac = Board()


#Display board at the beginning
tictac.displayBoard()

# Run game while not over
while not tictac.gameover:
    tictac.nextTurn()