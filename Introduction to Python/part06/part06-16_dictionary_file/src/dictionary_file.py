# Write your solution here
def reading_file():
    with open("dictionary.txt") as dictionary:
        for line in dictionary:
            line = line.strip()
            parts = line.split(": ")
            
            words[parts[0]] = parts[1]

def add_word():
    finnish = input("The word in Finnish: ")
    english = input("The word in English: ")
    
    words[finnish] = english
    
    dictionary.write(f"{finnish}: {english}\n")
    
    print("Dictionary entry added")
    
def search_word():
    search_term = input("Search term: ")
    
    for word, translation in words.items():
        if search_term in word or search_term in translation:
            print(f"{word} - {translation}")

with open("dictionary.txt", "a") as dictionary:
    words = {}
    reading_file()
    while True:
        print("1 - Add word, 2 - Search, 3 - Quit")
        function = int(input("Function: "))
        
        if function == 1:
            add_word()
        elif function == 2:
            search_word()
        elif function == 3:
            print("Bye!")
            break