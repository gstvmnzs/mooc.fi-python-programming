# Write your solution here
from string import ascii_lowercase, digits
from random import choice


def generate_strong_password(length:int, numbers:bool, special_chars:bool):
    specials = "!?=+-()#"
    password = ""
    password += choice(ascii_lowercase)
    if numbers:
        password += choice(digits)
    if special_chars:
        password += choice(specials)
    letters_nums = ascii_lowercase + digits
    letters_special = ascii_lowercase + specials
    all_chars = ascii_lowercase + digits + specials
    
    for i in range(length-len(password)):
        if numbers:
            if special_chars:
                password += choice(all_chars)
            else:
                password += choice(letters_nums)
        elif special_chars:
            password += choice(letters_special)
        else:
            password += choice(ascii_lowercase)
        
    return password