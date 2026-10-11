# Write your solution here
layers = int(input("Layers: "))
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

size = layers * 2 - 1
center_index = size // 2

for row in range(size):
    current_row = ""
    for col in range(size):
        distance_row = abs(row - center_index)
        distance_col = abs(col - center_index)
        
        letter_index = max(distance_row, distance_col)
        current_row += letters[letter_index]
    print(current_row)