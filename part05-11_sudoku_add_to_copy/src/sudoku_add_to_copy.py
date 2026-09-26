# Write your solution here
def copy_and_add(sudoku:list, row_no: int, column_no: int, number: int):
    sudoku_copy = []
    for row in sudoku:
        line = []
        for square in row:
            line.append(square)
        sudoku_copy.append(line)
    
    sudoku_copy[row_no][column_no] = number
    
    return sudoku_copy
    