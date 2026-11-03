# Write your solution here
from random import sample

def words_into_list():
    word_list = []
    with open("words.txt") as words:
        for line in words:
            line = line.strip()
            word_list.append(line)
    return word_list

def words(n:int, beginning:str):
    word_list = words_into_list()
    words_with_beggining = []
    for word in word_list:
        if word.startswith(beginning):
            words_with_beggining.append(word)
    if len(words_with_beggining) < n:
        raise ValueError("There were less words than specified")
    random_words = sample(words_with_beggining, n)
    
    return random_words