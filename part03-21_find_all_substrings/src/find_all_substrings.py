# Write your solution here
word = input("Please type in a word: ")
character = input("Please type in a character: ")
index = word.find(character)

while index != -1 and len(word[index:index+3]) > 2:
    print(word[index:index+3])
    index = word.find(character, index+1)