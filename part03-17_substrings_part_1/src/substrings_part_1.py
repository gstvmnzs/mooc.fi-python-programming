# Write your solution here
word = input("Please type in a string: ")
substring = 0

while substring <= len(word):
    print(word[:substring])
    substring += 1
