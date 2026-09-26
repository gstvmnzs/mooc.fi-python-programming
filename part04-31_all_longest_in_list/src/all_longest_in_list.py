# Write your solution here
def all_the_longest(words):
    new = []
    item = words[0]
    for word in words:
        if len(word) > len(item):
            item = word
    for word in words:
        if len(word) == len(item):
            new.append(word)
    
    return new


if __name__ == "__main__":
    my_list = ['Alan', 'Steve', 'Seymour', 'Kim', 'Susan']

    result = all_the_longest(my_list)
    print(result) # ['eleventh']