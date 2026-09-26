# Write your solution here
def length_of_longest(words):
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    return len(longest)