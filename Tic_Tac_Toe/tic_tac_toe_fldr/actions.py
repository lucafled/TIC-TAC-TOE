# checks if there is a win or draw and informs about it 

def insertLetter(letter, position):
    if spaceIsFree(position):
        board[position] = letter
        printBoard(board)
        if (checkDraw()):
            print("Draw!")
            exit()
        if checkForWin():
            if letter == 'X':
                print("X wins !")
                exit()
            else:
                print("O wins!")
                exit()  
              return
            
        else:
        print("already something here :(")
        position = int(input("Choose somewhere else :) "))
        insertLetter(letter, position)
        return
        
#################################################################################################
# chooses the game for a draw

def checkDraw():
    for key in board.keys():
        if (board[key] == ' '):
            return False
    return True

#################################################################################################
# chooses the position for "O"

def playerMove():
    position = int(input("Choose the position for 'O':  "))
    insertLetter(player, position)
    return

#################################################################################################
# chooses the position for "X"

def compMove():
    position = int(input("Choose the position for 'X':  "))
    insertLetter(bot, position)
    return

printBoard(board)

#################################################################################################
# is the loop that permits the game to run until a win or draw is achieved 

while not checkForWin():
    compMove()
    playerMove()
