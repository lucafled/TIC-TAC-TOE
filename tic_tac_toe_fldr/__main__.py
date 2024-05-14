# reference links  ->
# https://www.youtube.com/watch?v=dK6gJw4-NCo
# author: Code Coach


# https://www.youtube.com/watch?v=M3G1ZgOMFxo
# author: Shaun Halverson


checkhi = 'hi'
check = 'ok'

# instructions
for instructions in check:
    if instructions == "hi":
        continue
    print(input('Hi, welcome to tic tac toe (write "hi" to continue):'))
    break

for instructions in check:
    if instructions == "ok":
        continue
    print(input('In order to win the game, complete 3 spaces in diagonal or a straight line by inputting a position with the corresponding number (write "ok" to continue):'))
    break

for instructions in check:
    if instructions == "ok":
        continue
    print(input('For example, if you want to select the position at the right top coorner, input a 3 (write "ok" to continue):'))
    break


plrO = 'O'
plrX = 'X'

from actions import checkForWin, compMove, playerMove
from actions import insertLetter, playerMove, compMove
from actions import checkForWin, playerMove, compMove, reset, checkForDraw



# Game loop
while True:
    while not checkForWin():
        compMove()
        if checkForWin():
            break
        playerMove()
