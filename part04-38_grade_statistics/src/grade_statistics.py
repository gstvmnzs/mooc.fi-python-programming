def user_inputs():
    results = []
    while True:
        user = input()
        if user == "":
            break
        results.append(user)
    for i in range(len(results)):
        results[i] = results[i].split()
        results[i][0] = int(results[i][0])
        results[i][1] = int(results[i][1])
    return results

def filter_data(results):
    for i in range(len(results)):
        results[i][1] = results[i][1]//10
    total_points = []
    for item in results:
        total_points.append(sum(item))
    average = f"{(sum(total_points)/len(total_points)):.1f}"
    return average, results

def statistics(average, results):
    for i in range(len(results)):
        if results[i][0] < 10:
            results[i] = 0
        else:
            results[i] = sum(results[i])
    grade_0 = ""
    grade_1 = ""
    grade_2 = ""
    grade_3 = ""
    grade_4 = ""
    grade_5 = ""
    
    counter = len(results)
    for item in results:
        if item >= 28:
            grade_5 += "*"
        elif item >=24:
            grade_4 += "*"
        elif item >= 21:
            grade_3 += "*"
        elif item >= 18:
            grade_2 += "*"
        elif item >= 15:
            grade_1 += "*"
        else: 
            counter -= 1
            grade_0 += "*"
            
    pass_percentage = f"{(counter/len(results)*100):.1f}"
    
    print(f'''
            Statistics: 
            Points average: {average}
            Pass percentage: {pass_percentage}
            Grade distribution: 
              5: {grade_5}
              4: {grade_4}
              3: {grade_3}
              2: {grade_2}
              1: {grade_1}
              0: {grade_0}''')
    
inputs = user_inputs()
average, results = filter_data(inputs)
statistics(average, results)