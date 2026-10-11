# write your solution here
file1 = input("Student information: ")
file2 = input("Exercises completed: ")

students_dict = {}
with open(file1) as students:
    for line in students:
        line = line.strip()
        line = line.split(";")
        
        if "id" in line:
            continue
        key = line[0]
        value = f"{line[1]} {line[2]}"
        students_dict[key] = value

total_exercises_completed = {}
with open(file2) as exercises:
    for line in exercises:
        line = line.strip()
        line = line.split(";")
        
        if "id" in line:
            continue
        key = line[0]
        total_exercises = 0
        for item in line[1:]:
            item = int(item)
            total_exercises += item
        total_exercises_completed[key] = total_exercises

for key, value in students_dict.items():
    if key in total_exercises_completed:
        exercises = total_exercises_completed[key]
        print(f"{value} {exercises}")