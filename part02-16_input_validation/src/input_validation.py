from math import sqrt

while True:
    user = int(input("Please type in a number: "))

    if user < 0:
        print("Invalid number")
    elif user == 0:
        print("Exiting...")
        break
    else:
        print(sqrt(user))