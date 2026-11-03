# Write your solution here
import urllib.request
import json


# print(my_request.read())

def retrieve_all():
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    data = my_request.read()
    courses = json.loads(data)
    
    active = []
    for course in courses:
        if course["enabled"] == True:
            total = 0
            for points in course["exercises"]:
                total += points
            active.append((course["fullName"], course["name"], course["year"], total))
    return active

def retrieve_course(course_name:str):
    my_request = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")
    data = my_request.read()
    course_json = json.loads(data)
    
    hours = 0
    max_students = []
    exercises = 0
    for info in course_json.values():
        max_students.append(info["students"])
        exercises += info["exercise_total"]
        hours += info["hour_total"]
    
    max_students = max(max_students)
    hours_average = hours // max_students
    exercises_average = exercises // max_students
    
    course_info = {
        "weeks": len(course_json),
        "students": max_students,
        "hours": hours,
        "hours_average": hours_average,
        "exercises": exercises,
        "exercises_average": exercises_average
    }
    
    return course_info