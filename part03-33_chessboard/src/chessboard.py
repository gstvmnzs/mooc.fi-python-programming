# Write your solution here
def chessboard(num):
    height = 1
    while height <= num:
        width = 1
        while width <= num and height % 2 == 1:
            if width % 2 == 1:
                print(1, end="")
            else:
                print(0, end="")
            width += 1
        while width <= num and height % 2 == 0:
                    if width % 2 == 1:
                        print(0, end="")
                    else:
                        print(1, end="")
                    width += 1
        print()
        height += 1

# Testing the function
if __name__ == "__main__":
    chessboard(3)
