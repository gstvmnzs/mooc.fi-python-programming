# Write your solution here
from difflib import get_close_matches

text = input("Write text: ")
text_words = text.split()

word_list = []
with open("wordlist.txt") as words:
    for word in words:
        word = word.strip().lower()
        word_list.append(word)
    for i in range(len(text_words)):
        if text_words[i].lower() not in word_list:
            text_words[i] = f"*{text_words[i]}*"

corrected = ""
for i in range(len(text_words)):
    if i < len(text_words)-1:
        corrected += f"{text_words[i]} "
    else:
        corrected += text_words[i]

print(corrected)

print("suggestions:")
parts = corrected.split()
for item in parts:
    suggestion_string = ""
    if "*" in item:
        wrong_word = item[1:len(item)-1]
        suggestion_string += f"{wrong_word}: "
        close = get_close_matches(wrong_word, word_list)
        for suggestion in close:
            suggestion_string += f"{suggestion}, "
        print(suggestion_string[:len(suggestion_string)-2])
    
