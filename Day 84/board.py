class Board:
    def __init__(self):
        self.slots = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.gameover = False
        self.player1Turn = True;

    # Display the board.
    def displayBoard(self):
        print(f'{self.slots[0]} |{self.slots[1]} |{self.slots[2]}')
        print(f'--------')
        print(f'{self.slots[3]} |{self.slots[4]} |{self.slots[5]}')
        print(f'--------')
        print(f'{self.slots[6]} |{self.slots[7]} |{self.slots[8]}')

    # Check if selected index is valid.
    # Insert if valid
    def insertIndex(self, index):
        #Index outside valid area.
        if (index > 8 or index < 0):
            print("invalid index")
            return False
        else:
            #Check if index is not taken by opponent
            if (self.slots[index] == ' '):
                #Check whose players turn
                #Player 1: X
                #Player 2: O
                if (self.player1Turn):
                    self.slots[index] = 'X'
                else:
                    self.slots[index] = 'O'
                return True
            else:
                print("Spot already taken")
                return False

    # Validate if the game is finished or there is a winner
    # This involves the most logic.
    def validate(self):
        # Check all horizontal rows
        def validate_horizontal(toCheck):
            for ln in range(0, 3):
                if (self.slots[ln * 3] == toCheck and self.slots[ln * 3 + 1] == toCheck and self.slots[
                    ln * 3 + 2] == toCheck):
                    return True
            return False;
        # Check all vertical rows
        def validate_vertical(toCheck):
            for ln in range(0, 3):
                if (self.slots[ln] == toCheck and self.slots[ln + 3] == toCheck and self.slots[ln + 6] == toCheck):
                    return True
                    break
            return False;
        # Check all diagonal
        def validate_diagonal(toCheck):
            if(self.slots[0]== toCheck and self.slots[4]== toCheck and self.slots[8]== toCheck):
                return True
            if(self.slots[2]== toCheck and self.slots[4]== toCheck and self.slots[6]== toCheck):
                return True
            return False

        if(self.player1Turn):
            valHor = validate_horizontal("X")
            valVer = validate_vertical("X")
            valDia = validate_diagonal("X")
            print("valHor",valHor)
            print("valVer", valVer)
            print("valDia", valDia)
            if(valHor or valVer or valDia):
                self.gameover = True
        else:
            valHor = validate_horizontal("O")
            valVer = validate_vertical("O")
            valDia = validate_diagonal("v")
            if (valHor or valVer or valDia):
                self.gameover = True

    #Check if there is still a next turn
    def checkNextTurn(self):
        stillValid = False
        for index in self.slots:
            if(index == ' '):
                stillValid = True
                break;
        return stillValid


    # Ask for an index for a turn
    # Check if valid, insert if valid.
    def nextTurn(self):
        print(f"{'Player 1' if self.player1Turn == True else 'Player 2'} turn.")
        index = input("Input index of where you want to place your marker?")
        # Attempt an insert
        isInserted = self.insertIndex(index=int(index))
        # If insert is valid, switch players
        if (isInserted):
            # Validate if game is over or there is a winner
            self.validate()
            #If game is not over, change players
            if(not self.gameover):
                self.player1Turn = False if self.player1Turn == True else True
        # Display updated board
        self.displayBoard()

        if(self.gameover):
            print(f"{'Player 1' if self.player1Turn == True else 'Player 2'} won the game.")
            print("Thanks for playing")
        else:
            if(not self.checkNextTurn()):
                print("No more valid moves. Game over")
                self.gameover = True