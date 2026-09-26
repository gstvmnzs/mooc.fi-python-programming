# Write your solution here
def double_items(numbers: list):
    new_list = []
    for item in numbers:
        item *= 2
        new_list.append(item)
    return new_list