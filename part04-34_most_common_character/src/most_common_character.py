# Write your solution here
def most_common_character(word):
    frequency = 0
    moment = ""
    for char in word:
        times = word.count(char)
        if times > frequency:
            frequency = times
            moment = char
    return moment

if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))