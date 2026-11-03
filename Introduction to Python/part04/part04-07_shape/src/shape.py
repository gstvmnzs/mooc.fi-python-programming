# Copy here code of line function from previous exercise and use it in your solution
def line(num, word):
    if word == "":
        print("*" * num)
    else:
        print(word[0] * num)

# You can test your function by calling it within the following block
def shape(width, char_tri, rec_height, char_rec):
    i = 1
    while i <= width:
        line(i, char_tri)
        i += 1
    while rec_height > 0:
        line(width, char_rec)
        rec_height -= 1

if __name__ == "__main__":
    shape(5, "x", 3, "*")