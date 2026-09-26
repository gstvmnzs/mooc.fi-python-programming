# Write your solution here
sentence = input("Please type in a sentence: ")
pos = sentence.find(" ")

while True:
    print(sentence[0])
    pos = sentence.find(" ")
    if pos == -1:
        break
    sentence = sentence[pos+1:]
