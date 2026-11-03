# tee ratkaisu tänne
# write your solution here
student_info = input("Student information: ")
exercises_completed = input("Exercises completed: ")
exam_points = input("Exam points: ")

students_dict = {}
with open(student_info) as students:
    for line in students:
        line = line.strip()
        line = line.split(";")
        
        if "id" in line:
            continue
        key = line[0]
        value = f"{line[1]} {line[2]}"
        students_dict[key] = value

total_exercises_completed = {}
with open(exercises_completed) as exercises:
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
        exercise_points = total_exercises / 40 * 100 // 10
        total_exercises_completed[key] = [total_exercises, exercise_points]
    
exam_total_points = {}
with open(exam_points) as exam:
    for line in exam:
        line = line.strip()
        line = line.split(";")
        
        if "id" in line:
            continue
        key = line[0]
        grades = []
        for item in line[1:]:
            item = int(item)
            grades.append(item)
        total = sum(grades)
        exam_total_points[key] = total

     
print(f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10}")
for key, value in students_dict.items():
    if key in total_exercises_completed and key in exam_total_points:
        points = exam_total_points[key] + total_exercises_completed[key][1]
        if points < 15:
            grade = 0
        elif points < 18:
            grade = 1
        elif points < 21:
            grade = 2
        elif points < 24:
            grade = 3
        elif points < 27:
            grade = 4
        else:
            grade = 5
    
        print(f"{value:30}{total_exercises_completed[key][0]:<10}{int(total_exercises_completed[key][1]):<10}{exam_total_points[key]:<10}{int(points):<10}{grade:<10}")