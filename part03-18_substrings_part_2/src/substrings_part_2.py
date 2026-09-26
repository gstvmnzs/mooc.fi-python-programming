# Write your solution here
word = input("Please type in a string: ")

length = -1
while length >= -len(word):
    print(word[length:])
    length -= 1