# Write your solution here
input_string1 = input("Please type in string 1: ")
input_string2 = input("Please type in string 2: ")

if len(input_string1) > len(input_string2):
    print(f"{input_string1} is longer")
elif len(input_string2) > len(input_string1):
    print(f"{input_string2} is longer")
else:
    print("The strings are equally long")