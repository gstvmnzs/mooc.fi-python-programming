word = input("Please type in a string: ")
substring = input("Please type in a substring: ")

first = word.find(substring)

if first == -1:
    print("The substring does not occur twice in the string.")
else:
    second = word.find(substring, first + len(substring))

    if second == -1:
        print("The substring does not occur twice in the string.")
    else:
        print(f"The second occurrence of the substring is at index {second}.")