# Write your solution here
from random import choice


def roll(die:str):
    die_a = [3, 3, 3, 3, 3, 6]
    die_b = [2, 2, 2, 5, 5, 5]
    die_c = [1, 4, 4, 4, 4, 4]
    if die == "A":
        result = choice(die_a)
    elif die == "B":
        result = choice(die_b)
    elif die == "C":
        result = choice(die_c)
        
    return result

def play(die1:str, die2:str, times:int):
    p1 = 0
    p2 = 0
    tie = 0
    
    for i in range(times):
        roll1 = roll(die1)
        roll2 = roll(die2)
        
        if roll1 > roll2:
            p1 += 1
        elif roll2 > roll1:
            p2 += 1
        elif roll1 == roll2:
            tie += 1
        
    return (p1, p2, tie)