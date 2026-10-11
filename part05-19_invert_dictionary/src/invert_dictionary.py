# Write your solution here
def invert(dictionary: dict):
    new_dict = {}
    for key, value in dictionary.items():
        new_dict[value] = key
    dictionary.clear()
    for key, value in new_dict.items():
        dictionary[key] = value
        