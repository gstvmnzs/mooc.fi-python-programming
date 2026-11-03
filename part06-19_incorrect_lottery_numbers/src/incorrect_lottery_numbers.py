# Write your solution here

def file_into_dict():
    lottery_dict = {}
    with open("lottery_numbers.csv") as lottery:
        for line in lottery:
            line = line.strip()
            parts = line.split(";")
            
            numbers = parts[1].split(",")
            nums = []
            for item in numbers:
                try:
                    nums.append(int(item))
                except ValueError:
                    continue
            
            lottery_dict[parts[0]] = nums
    return lottery_dict

def filter_incorrect():
    dictionary = file_into_dict()
    with open("correct_numbers.csv", "w") as correct:
        for key, value in dictionary.items():
            write = ""
            try:
                week_test = key.split(" ")
                week_num = int(week_test[1])
            except ValueError:
                continue
            write += f"{key};"
            if len(value) != 7:
                continue
            nums = []
            problem = False
            for i in range(7):
                if value[i] in nums or value[i] not in range(1, 40):
                    problem = True
            
                if problem != True:
                    nums.append(value[i])
                    write += f"{value[i]},"
                else: 
                    break
            if problem != True:
                write = write[0:len(write)-1]
                correct.write(f"{write}\n")