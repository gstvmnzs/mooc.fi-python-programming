# write your solution here
def create_matrix():
    matrix = []
    with open("matrix.txt") as file:
        for line in file:
            line = line.replace("\n", "")
            parts = line.split(",")
            
            row = []
            for num in parts:
                num = int(num)
                row.append(num)
            matrix.append(row)
    return matrix


def matrix_sum():
    matrix = create_matrix()
    
    total = 0
    for row in matrix:
        total += sum(row)
    return total


def matrix_max():
    matrix = create_matrix()
    
    max_value = None
    for row in matrix:
        max_row = max(row)
        if max_value == None or max_value < max_row:
            max_value = max_row
    return max_value

def row_sums():
    matrix = create_matrix()
    
    row_sums = []
    for row in matrix:
        row_sums.append(sum(row))
    return row_sums