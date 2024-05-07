# reference links  ->
# https://www.youtube.com/watch?v=dK6gJw4-NCo
# author: Code Coach


# https://www.youtube.com/watch?v=M3G1ZgOMFxo
# author: Shaun Halverson






checkhi = 'hi'
check = 'ok'



for instructions in check:
   if instructions == "hi":
       continue  # This skips the current iteration and moves to the next one
   print (input('Hi welcome to tic tac toe (write "hi" to continue):'))
   break


for instructions in check:
   if instructions == "ok":
       continue  # This skips the current iteration and moves to the next one
   print (input('In order to win the game complete 3 spaces in diagonal or a straight line by inputing a position with the corresponding number (write "ok" to continue):'))
   break


from board import squares_board, gameboard
from actions import insertLetter, playerMove, compMove
from actions import checkForWin, playerMove, compMove, checkForDraw    #all the checks




while not checkForWin():
   compMove()
   playerMove()
else:
   if checkForWin == True:
    instructions
