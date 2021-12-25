# This is the main file which holds functions to modify the board and
# build the backtracking algo

def create_board(): 
    board = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
    ]
    return board

def solve_board(board):
    find = find_empty(board)
    if not find:
        return True # no more spots to fill up
    else:
        row, col = find

    # Try all values in empty spot
    for i in range(1, 10): 
        # If val is valid, then put it in 
        if is_valid(board, i, (row, col)):
            board[row][col] = i 
            # then move onto next and try finishing board
            if solve_board(board): 
                return True    
            board[row][col] = 0

    # if return false, try next value 
    return False



def print_board(board): 
    for i in range(len(board)):
        if (i % 3 == 0) and i != 0 :
            print(" - - - - - - - - - - - - - -")

        for j in range(len(board[0])):
            if (j % 3 == 0): 
                print(" | ", end = "")
            if j == 8: 
                print(str(board[i][j]) + " | ")
            else:
                print(str(board[i][j]) + " ", end = "")

def find_empty(board):
    for i in range(len(board)):
        for j in range(len((board[0]))):
            if board[i][j] == 0:
                return (i, j) # row, col
    return None

def is_valid(board, num, pos):
    # Validate row
    # check every element and skip the spot you just inserted into
    for i in range(len(board[0])): 
        if board[pos[0]][i] == num and pos[1] != i: 
            return False

    # Validate column; same thing but down
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i: 
            return False

    # Validate box/quadrant
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range (box_y  * 3,  box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    
    return True

