# Write your solution here 
word = input("Word: ")

print("*" * 30)
if len(word) % 2 == 0:
    print("*" + (int(((28 - len(word))/2)) * " ") + word + (int(((28 - len(word))/2)) * " ") + "*")
else:
    print("*" + (int(((28 - len(word))/2)) * " ") + word + (int(((28 - len(word))/2 + 1)) * " ") + "*")
print("*" * 30)