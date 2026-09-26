# Write your solution here
my_list = []
items_to_be_added = int(input("How many items: "))

x = 1
while 1 <= items_to_be_added:
    value = int(input(f"item {x}: "))
    my_list.append(value)
    x += 1
    items_to_be_added -= 1
print(my_list)