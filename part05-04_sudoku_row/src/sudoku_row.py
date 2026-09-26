# Write your solution here
def row_correct(sudoku: list, row_no: int):
    numbers = []
    for number in sudoku[row_no]:
        if number > 0 and number not in numbers:
            numbers.append(number)
        elif number in numbers:
            return False
    return True