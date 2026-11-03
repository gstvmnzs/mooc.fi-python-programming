# Write your solution here
import csv
import datetime

def final_points():
    start_times = {}
    with open("start_times.csv") as start, open("submissions.csv") as submissions:
        for line in csv.reader(start, delimiter=";"):
            start_times[line[0]] = datetime.datetime.strptime(line[1], "%H:%M")
        tasks = {}
        for line in csv.reader(submissions, delimiter=";"):
            name = line[0]
            task_num = line[1]
            points = int(line[2])
            submission = datetime.datetime.strptime(line[3], "%H:%M")       
            
            if submission - start_times[name] > datetime.timedelta(hours=3):
                continue
            if name in tasks:
                if f"task {task_num}" not in tasks[name]:
                    tasks[name][f"task {task_num}"] =  points
                else:
                    tasks[name][f"task {task_num}"] = max(tasks[name][f"task {task_num}"], points)
            else:
                tasks[name] = {f"task {task_num}": points}
        
        final_dict = {}
        for name, task_no in tasks.items():
            points_list = []
            for points in task_no.values():
                points_list.append(points)
            final_dict[name] = sum(points_list)
            
    return final_dict
        
            
            
           