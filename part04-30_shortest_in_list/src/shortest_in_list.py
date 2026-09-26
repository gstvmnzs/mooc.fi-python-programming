# Write your solution here
def shortest(words):
    shortest = words[0]
    for word in words:
        if len(word) < len(shortest):
            shortest = word
    return shortest