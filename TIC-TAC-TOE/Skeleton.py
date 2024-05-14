# print the game board 
squares_board = {1: ' ', 2: ' ', 3: ' ',
                4: ' ', 5: ' ', 6: ' ',
                7: ' ', 8: ' ', 9: ' '}
check = 'ok'

for instructions in check:
    if instructions == "ok":
        continue  # This skips the current iteration and moves to the next one
    print (input('Hi welcome to tic tac toe, in order to win the game complete 3 spaces in diagonal or a straight line (write "ok" to continue):'))


def gameboard (squares_board):
    print(squares_board[1] + '|' + squares_board[2] + '|' + squares_board[3])
    print('-+-+-')
    print(squares_board[4] + '|' + squares_board[5] + '|' + squares_board[6])
    print('-+-+-')
    print(squares_board[7] + '|' + squares_board[8] + '|' + squares_board[9])
    print("\n")



# input the square to be selected°° 
X = 'xplr'
O = 'oplr'

def Xplyer():
    X = int (input ("X move:"))

def Oplyer():
    O = int (input ("O move:"))

   
        
    
# check for win 
def win():
    if X or O == 1 == 2 == 3: 
        if X or O == 1 == 4 == 7:
             if X or O == 1 == 5 == 9: 
                if X or O ==2 == 5 == 8: 
                    if X or O == 3 == 6 == 9: 
                        if X or O == 3 == 5 == 7:
                            if X or O ==7 == 8 == 9 :
                                return True
        
if X == win():
    print ('You Won X!!')
else:
    print ('You Won O!!')
 



# if a square is occupied let the user know
if X == O:
    print ("already something here")






# reference links  ->
# https://www.youtube.com/watch?v=dK6gJw4-NCo
# author: Code Coach

# https://www.youtube.com/watch?v=M3G1ZgOMFxo
# author: Shaun Halverson
