# Write your solution here
num = int(input("Please type in a number: "))

follow = 1
while True and num != 1:
    print(follow+1)
    print(follow)
    follow += 2
    if follow == num:
        print(num)
        break
    elif follow > num:
        break
if num == 1:
    print(follow)