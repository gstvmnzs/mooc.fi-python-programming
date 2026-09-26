# Write your solution here
def spruce(size):
    print("a spruce!")
    height = 1
    i = 1
    space_ammount = size - 1
    while height <= size:
        print(" " * space_ammount + "*" * i)
        i += 2
        height += 1
        space_ammount -= 1
    print(" " * (size-1) + "*")


# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)