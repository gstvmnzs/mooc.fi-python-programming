# Write your solution here
def sudoku_grid_correct(sudoku: list):
    for i in range(9):
        if row_correct(sudoku, i) == False:
            return False
    for i in range(9):
        if column_correct(sudoku, i) == False:
            return False
    for i in range(0, 9, 3):
        for x in range(0, 9, 3):
            if block_correct(sudoku, i, x) == False:
                return False
    return True
        
    
def block_correct(sudoku: list, row_no: int, column_no: int):
    numbers = []
    for i in range(row_no, row_no + 3):
        for x in range(column_no, column_no + 3):
            if sudoku[i][x] > 0 and sudoku[i][x] in numbers:
                return False
            numbers.append(sudoku[i][x])
    return True

def column_correct(sudoku: list, column_no: int):
    numbers = []
    for row in sudoku:
        if row[column_no] > 0 and row[column_no] in numbers:
            return False
        numbers.append(row[column_no])
    return True

def row_correct(sudoku: list, row_no: int):
    numbers = []
    for number in sudoku[row_no]:
        if number > 0 and number not in numbers:
            numbers.append(number)
        elif number in numbers:
            return False
    return True