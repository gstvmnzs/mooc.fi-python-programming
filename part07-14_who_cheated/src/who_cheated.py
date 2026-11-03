# Write your solution here
def cheaters():
    import csv
    import datetime


    start_dict = {}
    with open("start_times.csv") as start_times:
        for line in csv.reader(start_times, delimiter=";"):
            start_dict[line[0]] = datetime.datetime.strptime(line[1], "%H:%M")
    
    with open("submissions.csv") as submissions:
        sub_dict = {}
        for line in csv.reader(submissions, delimiter=";"):
            if line[0] in sub_dict:
                sub_dict[line[0]] = max(sub_dict[line[0]], datetime.datetime.strptime(line[3], "%H:%M"))
            else:
                sub_dict[line[0]] = datetime.datetime.strptime(line[3], "%H:%M")
    
    cheater = []
    for student, start in start_dict.items():
        if student in sub_dict and sub_dict[student] - start > datetime.timedelta(hours=3):
            cheater.append(student)
    
    return cheater