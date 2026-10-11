def store_personal_data(person: tuple):
    line = ""
    for data in person:
        line += f"{data};"
    line = line[:-1]
    with open("people.csv", "a") as people:
        people.write(f"{line}\n")