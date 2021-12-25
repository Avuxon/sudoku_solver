from tkinter import *
from time import sleep
from sudoku_solver import solve_board
from PIL import ImageTk, Image

root = Tk()
root.title("Sudoku Solver")
#root.iconbitmap("./metadata/sudoku_icon.ico")

main_img = ImageTk.PhotoImage(Image.open("./metadata/sodoku_solver_image.png"))
main_label = Label(image=main_img)
main_label.grid(row=0, column=0, rowspan=6)

def solve():
    board = load_values()
    solve_board(board)
    push_to_board(board)

def load_values():
	# Creates nested list of all values from GUI
    board = [[0 for i in range(9)] for x in range(9)]
    for row in range(9):
        for elem in range(9):
            board[row][elem] = boxes[row][elem].get()
	# Nested list comprehension - replaces all empty values with a 0 and converts all filled values to integers
    board = [[0 if value == '' else int(value) for value in line] for line in board]
    return board

def push_to_board(board):
	# Place Holder for Fold
	# Clears all existing values on GUI Sodoku Board
    clear()
    # Inserts values stored on nested list - board - onto the GUI Sodoku Board
    for i in range(9):
        for j in range(9):
                boxes[i][j].insert(0, board[i][j])

def clear():
    for row in boxes:
        for box in row:
            print(box)
            box.delete(0, END)
            print(box)

# Creates Buttons for on, off, check, exit, clear
button_solve = Button(root, text="Solve", padx=226, pady=16, command=solve)
button_clear = Button(root, text="Clear", padx=226, pady=16, command=clear)
button_exit = Button(root, text="Exit", command=root.quit, padx=230, pady=16)

# Places buttons created in previous block onto GUI using grid system
button_solve.grid(row=6, column=0, columnspan=2)
button_clear.grid(row=7, column=0, columnspan=2)
button_exit.grid(row=8, column=0, columnspan=2)

boxes = [[Entry(root, font=('Arial',32,'bold'), \
        justify="center", borderwidth=3, width=2) for x in range(9)] for i in range(9)]

for i in range(9):
    for j in range(9):
        # Places 81 Sudoku Boxes onto GUI using grid system
        boxes[i][j].grid(row = i , column = j + 3)

root.mainloop()