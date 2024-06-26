#https://www.youtube.com/watch?v=M3G1ZgOMFxo
#Shaun Halverson

#https://www.youtube.com/watch?v=dK6gJw4-NCo
#Code Coach

# Check if position is empty
from board import squares_board, gameboard


plrO = 'O'
plrX = 'X'


def spaceIsFree(position):
    return squares_board[position] == ' '


# Insert a letter at a position
def insertLetter(letter, position):
    if spaceIsFree(position):
        squares_board[position] = letter
        gameboard(squares_board)
        if checkForWin():
            print(f'٩(˘◡˘)۶{letter} wins!٩(˘◡˘)۶')
            reset()
        elif checkForDraw():
            print("¯\\_( ͡❛ ● ͡❛)_/¯  Draw! ¯\\_( ͡❛ ● ͡❛)_/¯")
            reset()
        return
    else:
        print("already something here ┏( ͡❛ ︵ ͡❛)┛")
        position = int(input("Choose somewhere else ┏( ͡❛ ● ͡❛)┛ "))
        insertLetter(letter, position)
# we made a function to check for a win or draw. If there's a win, it prints a victory message and resets the game

# Check for a win
def checkForWin():
    win_conditions = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Columns
        [1, 5, 9], [3, 5, 7]              # Diagonals
    ]
    for condition in win_conditions:
        if all(squares_board[pos] == 'X' for pos in condition) or all(squares_board[pos] == 'O' for pos in condition):
            return True
    return False
    #checks for the winner if a condition is completed, If all positions in that condition have the same symbol the player wins 


# Check for a draw
def checkForDraw():
    return all(square != ' ' for square in squares_board.values())


# Request movement from 'X' (player)
def compMove():
    position = int(input("Choose the position for 'X': "))
    insertLetter(plrX, position)
    return


# Request movement from 'O' (player)
def playerMove():
    position = int(input("Choose the position for 'O':  "))
    insertLetter(plrO, position)
    return
#In here we check let the players chose a position 


# Reset the game
def reset():
    global squares_board
    play_again = input("Play again? (yes/no): ") # in this part we just ask the player if he wants to continue playing 
    if play_again == 'yes':
        squares_board = {1: ' ', 2: ' ', 3: ' ',
                         4: ' ', 5: ' ', 6: ' ',
                         7: ' ', 8: ' ', 9: ' '}
    else:
        exit()
