# Copy here code of line function from previous exercise
def line(num, word):
    if word == "":
        print("*" * num)
    else:
        print(word[0] * num)

def square_of_hashes(size):
    i = 1
    while i <= size:
        line(size, "#")
        i += 1
        

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
