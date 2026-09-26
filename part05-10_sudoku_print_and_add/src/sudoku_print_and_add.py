# Write your solution here
def print_sudoku(sudoku: list):
    for index_row in range(9):
        for index_column in range(9):
            if sudoku[index_row][index_column] == 0:
                sudoku[index_row][index_column] = "_"
    count_row = 0
    for row in sudoku:
        count_column = 0
        for square in row:
            count_column += 1
            if count_column % 3 == 0:
                print(square, end="  ")
            else:
                print(square, end=" ")
        count_row += 1
        if count_row % 3 == 0:
            print()
        print()

def add_number(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku[row_no][column_no] = number
    