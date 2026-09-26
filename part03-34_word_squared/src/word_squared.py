# Write your solution here
def squared(text, num):
    height = 1
    text *= num * num
    while height <= num:
        print(text[:num])
        text = text[num:]
        height += 1

if __name__ == "__main__":
    squared('ab', 3)