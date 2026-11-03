# write your solution here
def read_fruits():
    with open("fruits.csv") as file:
        fruits = {}
        for line in file:
            line = line.replace("\n", "")
            parts = line.split(";")
            fruit_name = parts[0]
            fruit_price = parts[1]
            fruits[fruit_name] = float(fruit_price)
    return fruits