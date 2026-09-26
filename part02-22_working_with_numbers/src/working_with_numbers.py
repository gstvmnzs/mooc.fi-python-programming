# Write your solution here

count = 0
count_neg = 0
count_pos = 0
sum = 0
print("Please type in integer numbers. Type in 0 to finish.")
while True:
    num = int(input("Number: "))

    if num == 0:
        break
    elif num < 0:
        count_neg += 1
    else:
        count_pos += 1

    sum += num
    count += 1
mean = sum / count

print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {sum}")
print(f"The mean of the numbers is {mean}")
print(f"Positive numbers {count_pos}")
print(f"Negative numbers {count_neg}")