# Write your solution here
def create_tuple(x: int, y: int, z: int):
    smallest = None
    greatest = None
    total = 0
    
    if x < y and x < z:
        smallest = x
    elif y < z:
        smallest = y
    else:
        smallest = z
    
    if x > y and x > z:
        greatest = x
    elif y > z:
        greatest = y
    else:
        greatest = z
    
    total = x + y + z
    
    tup = (smallest, greatest, total)
    
    return tup