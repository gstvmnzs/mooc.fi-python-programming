# Write your solution here
import datetime

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

date_of_birth = datetime.datetime(year, month, day)
eve = datetime.datetime(1999, 12, 31)

if eve < date_of_birth:
    print("You weren't born yet on the eve of the new millennium.")
else:
    age = (eve - date_of_birth).days
    print(f"You were {age} days old on the eve of the new millennium.")