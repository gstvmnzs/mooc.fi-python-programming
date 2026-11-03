# Write your solution here
def is_it_valid(pic:str):
    import datetime
    string = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    
    valid = True
    if len(pic) != 11:
        return False

    
    if pic[6] != "+" and pic[6] != "-" and pic[6] != "A":
        return False
    elif pic[6] == "+":
        start = "18"
        parts = pic.split("+")
    elif pic[6] == "-":
        start = "19"
        parts = pic.split("-")
    else:
        start = "20"
        parts = pic.split("A")
        
    day = parts[0][:2]
    month = parts[0][2:4]
    year = parts[0][4:]
    
    try:
        date_of_birth = datetime.datetime(int(f"{start}{year}"), int(month), int(day))
        current = datetime.datetime.now()

        if current < date_of_birth:
            valid = False
    except ValueError:
        valid = False
    
    nine_digit = int(f"{day}{month}{year}{parts[1][:3]}")
    index = nine_digit % 31
    if string[index] != pic[10]:
        valid = False
    
    return valid