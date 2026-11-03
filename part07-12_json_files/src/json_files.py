# Write your solution here
def print_persons(filename: str):
    import json
    with open(filename) as file:
        data = file.read()
        students = json.loads(data)
        
        for item in students:
            hobbies = ""
            for hobby in item["hobbies"]:
                hobbies += f"{hobby}, "
            hobbies = hobbies[:len(hobbies)-2]
            print(f'{item["name"]} {item["age"]} years ({hobbies})')