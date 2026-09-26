# Write your solution here

password = input("Password: ")
while True:
    confirmation = input("Repeat password: ")
    if password == confirmation:
        print("User account created!")
        break
    else:
        print("They do not match!")