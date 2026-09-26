# Write your solution here
def remove_smallest(numbers: list):
    smallest = numbers[0]
    for item in numbers:
        smallest = min(smallest, item)
    numbers.remove(smallest)
    
