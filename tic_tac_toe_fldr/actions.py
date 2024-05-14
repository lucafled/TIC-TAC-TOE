from board import squares_board, gameboard
plrO = 'O'
plrX = 'X'

# if position is empty let the other code know
def spaceIsFree(position):
   if squares_board[position] == ' ':
       return True
   else:
       return False
  


#if someone wins do this
dancex = ["┏( ͡❛ ͜ʖ ͡❛)┛ X wins! ┏( ͡❛ ͜ʖ ͡❛)┛", "┛( ͡❛ ͜ʖ ͡❛)┏ X wins! ┛( ͡❛ ͜ʖ ͡❛)┏", ]
danceo = ["┏( ͡❛ ͜ʖ ͡❛)┛ O wins! ┏( ͡❛ ͜ʖ ͡❛)┛", "┛( ͡❛ ͜ʖ ͡❛)┏ O wins! ┛( ͡❛ ͜ʖ ͡❛)┏", ]
repeat_times = 3





def insertLetter(letter, position):
   if spaceIsFree(position):
       squares_board[position] = letter
       gameboard(squares_board)
       if (checkForDraw()):
           print("¯\\_( ͡❛ ● ͡❛)_/¯  Draw! ¯\\_( ͡❛ ● ͡❛)_/¯")
           exit()
       if checkForWin():
           if letter == 'X':
               for d in dancex:
                   for _ in range(repeat_times):
                       print (dancex)
               exit()
           else:
               for d in danceo:
                   for _ in range(repeat_times):
                       print (danceo)
               exit()


       return
   else:
       print("already something here ┏( ͡❛ ︵ ͡❛)┛")
       position = int(input("Choose somewhere else ┏( ͡❛ ● ͡❛)┛ "))
       insertLetter(letter, position)
       return




#checks wins
def checkForWin():
   if (squares_board[1] == squares_board[2] and squares_board[1] == squares_board[3] and squares_board[1] != ' '):
       return True
   elif (squares_board[4] == squares_board[5] and squares_board[4] == squares_board[6] and squares_board[4] != ' '):
       return True
   elif (squares_board[7] == squares_board[8] and squares_board[7] == squares_board[9] and squares_board[7] != ' '):
       return True
   elif (squares_board[1] == squares_board[4] and squares_board[1] == squares_board[7] and squares_board[1] != ' '):
       return True
   elif (squares_board[2] == squares_board[5] and squares_board[2] == squares_board[8] and squares_board[2] != ' '):
       return True
   elif (squares_board[3] == squares_board[6] and squares_board[3] == squares_board[9] and squares_board[3] != ' '):
       return True
   elif (squares_board[1] == squares_board[5] and squares_board[1] == squares_board[9] and squares_board[1] != ' '):
       return True
   elif (squares_board[7] == squares_board[5] and squares_board[7] == squares_board[3] and squares_board[7] != ' '):
       return True
   else:
       return False
  


#checks draws
def checkForDraw():
   for key in squares_board.keys():
       if (squares_board[key] == ' '):
           return False
       return True   




#requests movement from x
def compMove():
   position = int(input("Choose the position for 'X': "))
   insertLetter(plrX, position)
   return


#request movement from 0
def playerMove():
   position = int(input("Choose the position for 'O':  "))
   insertLetter(plrO, position)
   return
gds



