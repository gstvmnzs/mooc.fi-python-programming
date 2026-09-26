# Write your solution here
num = int(input("Please type in a number: "))

operand1 = 1
while True:
    operand2 = 1
    while True:
        print(f"{operand1} x {operand2} = {operand1*operand2}")
        if operand2 == num:
            break
        operand2 += 1
    if operand1 == num:
        break
    operand1 += 1
    