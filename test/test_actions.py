checkhi = 'hi'
check = 'ok'

  
for instructions in check:
    if instructions == "hi":
        continue  
    print (input('Hi welcome to tic tac toe (write "hi" to continue):'))
    break

for instructions in check:
    if instructions == "ok":
        continue   
    print (input('In order to win the game complete 3 spaces in diagonal or a straight line by inputing a position with the corresponding number (write "ok" to continue):'))
    break





board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}
player = 'O'
bot = 'X'

def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print("\n")


def spaceIsFree(position):
    if board[position] == ' ':
        return True
    else:
        return False


dancex = ["┏( ͡❛ ͜ʖ ͡❛)┛ X wins! ┏( ͡❛ ͜ʖ ͡❛)┛", "┛( ͡❛ ͜ʖ ͡❛)┏ X wins! ┛( ͡❛ ͜ʖ ͡❛)┏", ]
danceo = ["┏( ͡❛ ͜ʖ ͡❛)┛ O wins! ┏( ͡❛ ͜ʖ ͡❛)┛", "┛( ͡❛ ͜ʖ ͡❛)┏ O wins! ┛( ͡❛ ͜ʖ ͡❛)┏", ]
repeat_times = 5


def insertposition(letter, position):
    if spaceIsFree(position):
        board[position] = letter
        printBoard(board)
        if (checkDraw()):
            print("¯\_( ͡❛ ● ͡❛)_/¯  Draw! ¯\_( ͡❛ ● ͡❛)_/¯")
            exit()
        if checkWin():
            if letter == 'X':
                for d in dancex:
                    for _ in range(repeat_times):
                        print (d)

                exit()
            else:
                for d in danceo:
                    for _ in range(repeat_times):
                        print (d)
                exit()

        return


    else:
        print("already something here ┏( ͡❛ ︵ ͡❛)┛")
        position = int(input("Choose somewhere else ┏( ͡❛ ● ͡❛)┛ "))
        insertposition(letter, position)
        return


def checkWin():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False


def checkDraw():
    for key in board.keys():
        if (board[key] == ' '):
            return False
    return True


def playerMove():
    position = int(input("Choose the position for 'O':  "))
    insertposition(player, position)
    return


def compMove():
    position = int(input("Choose the position for 'X':  "))
    insertposition
    (bot, position)
    return

printBoard(board)




while not checkWin():
    compMove()
    playerMove()





