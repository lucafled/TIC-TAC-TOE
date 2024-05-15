#https://www.youtube.com/watch?v=M3G1ZgOMFxo
#Shaun Halverson

#https://www.youtube.com/watch?v=dK6gJw4-NCo
#Code Coach


#board
squares_board= {1: ' ', 2: ' ', 3: ' ',
                4: ' ', 5: ' ', 6: ' ',
                7: ' ', 8: ' ', 9: ' '}

#printBoard
def gameboard(squares_board):
    print(squares_board[1] + '|' + squares_board[2] + '|' + squares_board[3])
    print('-+-+-')
    print(squares_board[4] + '|' + squares_board[5] + '|' + squares_board[6])
    print('-+-+-')
    print(squares_board[7] + '|' + squares_board[8] + '|' + squares_board[9])
    print("\n")

 
draw_doard = {1: 'X', 2: ' ', 3: 'X', 4: 'O', 5: 'O', 6: ' ', 7: 'X', 8: ' ', 9: 'O'}
squares_board_draw_empty = {1: 'X', 2: ' ', 3: 'X', 4: 'O', 5: 'O', 6: ' ', 7: 'X', 8: ' ', 9: 'O'}
squares_board_draw_full = {1: 'X', 2: 'O', 3: 'X', 4: 'O', 5: 'X', 6: 'O', 7: 'O', 8: 'X', 9: 'X'}


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


# Check for a draw
def checkForDraw():
    return all(square != ' ' for square in squares_board.values())


def spaceIsFree(position):
    return squares_board[position] == ' '

X_win_board = {1: 'X', 2: 'X', 3: 'X', 4: 'O', 5: 'O', 6: ' ', 7: ' ', 8: ' ', 9: ' '}

def test():
    squares_board_win = {1: 'X', 2: 'X', 3: 'X', 4: 'O', 5: 'O', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
    assert checkForWin(squares_board_win) == True
    if True:
        print ("squares_board_win")


def checkForWin(squares_board):
    win_conditions = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Columns
        [1, 5, 9], [3, 5, 7]              # Diagonals
    ]
    for condition in win_conditions:
        if all(squares_board[pos] == 'X' for pos in condition) or all(squares_board[pos] == 'O' for pos in condition):
            return True
    return False


def checkForDraw(squares_board):
    return all(square != ' ' for square in squares_board.values())


def spaceIsFree(squares_board, position):
    return squares_board[position] == ' '

##########################

#checks for wins
def test_for_win():
    squares_board_win = {1: 'X', 2: 'X', 3: 'X', 4: 'O', 5: 'O', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
    assert checkForWin(squares_board_win) == True
    if checkForWin(squares_board_win) == True:
        print('test for win succesful')
 

##########################

# tests for draws when true 
def test_draw():
    squares_board_draw = {1: 'X', 2: 'O', 3: 'X', 4: 'O', 5: 'X', 6: 'O', 7: 'O', 8: 'X', 9: 'X'}
    assert checkForWin(squares_board_draw) == False
    if checkForWin(squares_board_draw) == False:
        print('draw test succesful')

##########################

# tests for draws when false
def test_draw_2():
    squares_board_draw_full = {1: 'X', 2: 'O', 3: 'X', 4: 'O', 5: 'X', 6: 'O', 7: 'O', 8: 'X', 9: 'X'}
    assert checkForDraw(squares_board_draw_full) == True
    if checkForDraw(squares_board_draw_full) == True:
        print('draw test #2 (when not a draw) succesful ')
      

##########################

# test the free spaces
def test_space_free():
    assert spaceIsFree(squares_board_draw_empty, 2) == True
    if spaceIsFree(squares_board_draw_empty, 2) == True:
        print('free space test succesful')


##########################

# test the free spaces when there not free
def test_space_free2():
    assert spaceIsFree(squares_board_draw_full, 5) == False
    if spaceIsFree(squares_board_draw_full, 5) == False:
        print('free space test #2 (when not free) succesful')







test_for_win()
test_draw_2()
test_space_free()
test_space_free2()
