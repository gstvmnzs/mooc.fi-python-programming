# Write your solution here
width = int(input("Width: "))
height = int(input("Height: "))

control = 1
while control <= height:
    print("#" * width)
    control += 1