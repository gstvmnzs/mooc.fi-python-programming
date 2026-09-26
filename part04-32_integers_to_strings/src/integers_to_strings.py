# Write your solution here
def formatted(decimal_nums):
    new = []
    for num in decimal_nums:
        num = f"{num:.2f}"
        new.append(num)
    return new
    