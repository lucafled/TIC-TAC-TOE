#board
squares_board= {1: ' ', 2: ' ', 3: ' ',
                4: ' ', 5: ' ', 6: ' ',
                7: ' ', 8: ' ', 9: ' '}

player = 'O'
bot = 'X'


#printBoard
def gameboard(squares_board):
    print(squares_board[1] + '|' + squares_board[2] + '|' + squares_board[3])
    print('-+-+-')
    print(squares_board[4] + '|' + squares_board[5] + '|' + squares_board[6])
    print('-+-+-')
    print(squares_board[7] + '|' + squares_board[8] + '|' + squares_board[9])
    print("\n")

print (gameboard(squares_board))