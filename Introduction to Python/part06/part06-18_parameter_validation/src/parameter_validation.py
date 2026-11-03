# Write your solution here
def new_person(name:str, age:int):
    person = (name, age)
    
    if (len(person[0]) == 0 or len(person[0]) > 40 or " " not in person[0]) or (person[1] < 0 or person [1] > 150):
        raise ValueError("invalid age or name")
    
    return person