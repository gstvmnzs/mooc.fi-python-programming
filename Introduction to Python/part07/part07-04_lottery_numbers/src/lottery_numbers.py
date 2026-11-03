# Write your solution here
import random


def lottery_numbers(amount:int, lower:int, upper:int):
    number_pool = list(range(lower, upper+1))
    draw = random.sample(number_pool, amount)
    draw.sort()
    return draw
    
    