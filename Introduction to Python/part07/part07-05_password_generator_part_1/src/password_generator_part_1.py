# Write your solution here
from string import ascii_lowercase
from random import choice


def generate_password(length:int):
    password = ""
    for i in range(length):
        password += choice(ascii_lowercase)
    return password