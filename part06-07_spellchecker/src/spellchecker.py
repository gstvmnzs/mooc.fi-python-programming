# write your solution here
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
    if i < len(text_words) - 1:
        corrected += f"{text_words[i]} "
    else:
        corrected += text_words[i]
    
print(corrected)