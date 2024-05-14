


squares_board = {1: ' ', 2: ' ', 3: ' ',
                4: ' ', 5: ' ', 6: ' ',
                7: ' ', 8: ' ', 9: ' ',
                10: ' ', 11: ' ', 12: ' '}

def gameboard (squares_board):
    print(squares_board[1] + '|' + squares_board[2] + '|' + squares_board[3] + '|' + squares_board[4])
    print('-+-+-+-')
    print(squares_board[5] + '|' + squares_board[6] + '|' + squares_board[7]+ '|' + squares_board[8])
    print('-+-+-+-')
    print(squares_board[9]+ '|' + squares_board[10]+ '|' + squares_board[11] + '|' + squares_board[12])
    print("\n")

squares_board[1]= 'x'


print (gameboard(squares_board))

