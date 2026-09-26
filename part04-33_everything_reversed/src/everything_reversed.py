# Write your solution here
def everything_reversed(words):
    new = []
    i = len(words) -1
    while i >= 0:
        new.append(words[i][::-1])
        i -= 1
    return new

if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)