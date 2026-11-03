# write your solution here

def largest():
    with open("numbers.txt") as file:
        greatest = None
        
        for number in file:
            number = int(number)
            if greatest == None or number > greatest:
                greatest = number
    return greatest