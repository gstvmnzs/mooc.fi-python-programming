# Write your solution here
num = int(input("Please type in a number: "))

start = 1

while True:
    if num < start:
        break
    elif num == start:
        print(start)
        break
    print(start)
    print(num)
    num -= 1
    start +=1