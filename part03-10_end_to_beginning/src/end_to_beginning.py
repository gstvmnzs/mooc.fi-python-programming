# Write your solution here
user_string = input("Please type in a string: ")
control = -1

while control >= -len(user_string):
    print(user_string[control])
    control -= 1