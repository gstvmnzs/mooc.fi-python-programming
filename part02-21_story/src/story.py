# Write your solution here
phrase = ""
previous_word = ""

while True:
    word = input("Please type in word: ")
    if word == "end":
        break
    elif word == previous_word:
        break
    phrase += word + " "
    previous_word = word

print(phrase)