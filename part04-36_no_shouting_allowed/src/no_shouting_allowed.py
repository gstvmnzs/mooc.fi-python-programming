# Write your solution here
def no_shouting(words):
    new = []
    for word in words:
        if word.isupper() == False:
            new.append(word)
            
    return new
        