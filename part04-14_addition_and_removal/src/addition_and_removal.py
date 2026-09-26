# Write your solution here
my_list = []
print(f"The list is now {my_list}")
value_to_be_added = 1

while True:
    user = input("a(d)d, (r)emove or e(x)it: ")
    if user == "x":
        print("Bye!")
        break
    elif user == "d":
        my_list.append(value_to_be_added)
        value_to_be_added += 1
    elif user == "r":
        my_list.remove(value_to_be_added-1)
        value_to_be_added -= 1
    print(f"The list is now {my_list}")