# Write your solution here
cafeteria = int(input("How many times a week do you eat at the student cafeteria? "))
price = float(input("The price of a typical student lunch?"))
groceries = float(input("How much money do you spend on groceries in a week?"))

daily = cafeteria * price / 7 + groceries / 7
weekly = groceries + price * cafeteria

print(f'''
Average food expenditure:
Daily: {daily} euros
Weekly: {weekly} euros
''')