# Write your solution here

year = int(input("Year: "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    next = year + 4
    if next % 100 == 0 and next % 400 != 0: 
        next += 4
    print(f"The next leap year after {year} is {next}")
else:
    next = year + 1
    while True:
        if (next % 4 == 0 and next % 100 != 0) or next % 400 == 0:
            print(f"The next leap year after {year} is {next}")
            break
        next += 1