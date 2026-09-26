# Write your solution here
user_string = input("Please type in a string: ")


if len(user_string) > 1 and user_string[1] == user_string[-2]:
    print(f"The second and the second to last characters are {user_string[1]}")
else:
    print("The second and the second to last characters are different")