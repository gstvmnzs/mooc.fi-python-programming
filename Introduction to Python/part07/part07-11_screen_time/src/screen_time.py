# Write your solution here
import datetime

filename = input("Filename: ")
start = input("Starting date: ")
number_of_days = int(input("How many days: "))

with open(filename, "w") as file:
    start_date = datetime.datetime.strptime(start, "%d.%m.%Y")
    dif = datetime.timedelta(days=number_of_days - 1)
    end_date = start_date + dif
    file.write(f"Time period: {start_date.strftime("%d.%m.%Y")}-{end_date.strftime("%d.%m.%Y")}\n")

    data = {}
    increment = datetime.timedelta(days=1)
    for i in range(number_of_days):
        day_data = input(f"Screen time {start_date.strftime("%d.%m.%Y")}: ")
        data[start_date.strftime("%d.%m.%Y")] = day_data.replace(" ", "/")
        start_date += increment
        
    total = 0
    for value in data.values():
        parts = value.split("/")
        for item in parts:
            total += int(item)
    
    file.write(f"Total minutes: {total}\n")
    file.write(f"Average minutes: {total/number_of_days}\n")
        
    for key, value in data.items():
        file.write(f"{key}: {value}\n")
        
print(f"Data stored in file {filename}")
        
