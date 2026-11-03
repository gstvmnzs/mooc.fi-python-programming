# Write your solution here
import fractions


def fractionate(amount:int):
    equal_fractions = []
    number = fractions.Fraction(1, amount)
    for i in range(amount):
        equal_fractions.append(number)
    return equal_fractions