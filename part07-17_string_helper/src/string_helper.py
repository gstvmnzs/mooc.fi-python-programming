# Write your solution here
import string

def change_case(orig_string:str):
    new_str = ""
    
    for i in range(len(orig_string)):
        if orig_string[i] in string.ascii_lowercase:
            new_str += orig_string[i].upper()
        else:
            new_str += orig_string[i].lower()
            
    return new_str

def split_in_half(orig_string:str):
    length = len(orig_string)
    first_half = ""
    second_half = ""
    
    for i in range(length):
        if i <= length // 2 - 1:
            first_half += orig_string[i]
        else:
            second_half += orig_string[i]
        
    return(first_half, second_half)

def remove_special_characters(orig_string: str):
    no_special = ""
    allowed = string.ascii_uppercase + string.digits + string.ascii_lowercase + " "
    
    for i in range(len(orig_string)):
        if orig_string[i] not in allowed:
            continue
        no_special += orig_string[i]
        
    return no_special
            