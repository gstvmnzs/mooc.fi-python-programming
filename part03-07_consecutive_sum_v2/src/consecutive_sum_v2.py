# Write your solution here
# Write your solution here
limit = int(input("Limit: "))
start = 1
increment = 2
calculation = f"{start}"

while start < limit:
    start += increment
    calculation += f" + {increment}"
    increment += 1
    

print(f'The consecutive sum: {calculation} = {start}')
