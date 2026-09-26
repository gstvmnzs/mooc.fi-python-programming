# Write your solution here
def longest_series_of_neighbours(neighbors):
    length = 0
    counter = 0
    for i in range(1, len(neighbors)):
        if neighbors[i-1] - neighbors[i] == 1 or neighbors[i-1] - neighbors[i] == -1:
            counter += 1
        else:
            if counter + 1 > length:
                length = counter + 1
            counter = 0
    if counter + 1 > length:
        length = counter + 1
    return length