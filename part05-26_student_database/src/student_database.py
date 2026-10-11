# Write your solution here
def add_student(students: dict, student: str):
    students[student] = []

def print_student(students: dict, student: str):
    if student not in students:
        print(f"{student}: no such person in the database")
    else:
        print(f"{student}:")
        if len(students[student]) == 0:
            print(" no completed courses")
        else:
            print(f" {len(students[student])} completed courses:")
            total = 0
            for course in students[student]:
                print(f"  {course[0]} {course[1]}")
                total += course[1]
            print(f" average grade {total/len(students[student]):.1f}")
    
def add_course(students: dict, student: str, course_and_grade: tuple):
    found = False
    if course_and_grade[1] != 0:
        for i in range(len(students[student])):
            if course_and_grade[0] == students[student][i][0]:
                found = True
                if course_and_grade[1] > students[student][i][1]:
                    students[student][i] = course_and_grade
        if found == False:
            students[student].append(course_and_grade)
        
    
def summary(students):
    number_students = len(students)
    print(f"students {number_students}")
    
    most_courses = 0
    most_courses_person = None
    for student in students:
        if len(students[student]) > most_courses:
            most_courses = len(students[student])
            most_courses_person = student
    print(f"most courses completed {most_courses} {most_courses_person}")

    best_average = 0
    best_average_name = None
    for student, database in students.items():
        total = 0
        for course in database:
            total += course[1]
        average = total / len(database)
        if average > best_average:
            best_average = average
            best_average_name = student
    print(f"best average grade {best_average} {best_average_name}")