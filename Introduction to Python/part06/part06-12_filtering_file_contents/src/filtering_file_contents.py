# Write your solution here
def filter_solutions():
    with open("solutions.csv") as solutions, open("correct.csv", "w") as correct, open("incorrect.csv", "w") as incorrect:
        for line in solutions:
            row = line.split(";")
                
            equation = row[1]
            if "+" in equation:
                nums = equation.split("+")
                if int(nums[0]) + int(nums[1]) == int(row[2]):
                    correct.write(line)
                else:
                    incorrect.write(line)
            elif "-" in equation:
                nums = equation.split("-")
                if int(nums[0]) - int(nums[1]) == int(row[2]):
                    correct.write(line)
                else:
                    incorrect.write(line)