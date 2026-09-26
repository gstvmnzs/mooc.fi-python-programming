# Write your solution here
def transpose(matrix: list):
    for r in range(len(matrix[0])):
        for c in range(len(matrix[0])):
            if c > r:
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]