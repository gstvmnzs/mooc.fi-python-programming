# Write your solution here
def even_numbers(int_list):
    new_list = []
    for num in int_list:
        if num % 2 == 0:
            new_list.append(num)
    return new_list