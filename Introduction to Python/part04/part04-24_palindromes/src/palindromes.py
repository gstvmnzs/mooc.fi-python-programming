# Write your solution here
def palindromes(word):
    reverse = ""
    for i in range(len(word) - 1, -1, -1):
        reverse += word[i]
    return word == reverse

while True:
    palindrome = input("Please type in a palindome: ").lower()
    if palindromes(palindrome) == True:
        print(f"{palindrome} is a palindrome!")
        break
    print("that wasn't a palindrome")

# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
# if __name__ == "__main__":
    # palindromes("Python")