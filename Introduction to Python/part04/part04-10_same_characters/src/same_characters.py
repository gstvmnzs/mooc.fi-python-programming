# Write your solution here
def same_chars(text, num1, num2):
    if (num1 >= len(text) or num2 >= len(text)) or text[num1] != text[num2]:
        return False
    return text[num1] == text[num2]
        

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("abc", 0, 3))