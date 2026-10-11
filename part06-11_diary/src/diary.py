# Write your solution here
def function1(entry: str):
    with open("diary.txt", "a") as diary:
        diary.write(f"{entry}\n")
    print("Diary saved")

def function2():
    print("Entries:")
    with open("diary.txt") as diary:
        contents = diary.read()
        print(contents)

while True:
    print("1 - add entry, 2 - read entries, 0 - quit")
    function = int(input("Function: "))
    
    if function == 1:
        entry = input("Diary entry: ")
        function1(entry)
    elif function == 2:
        function2()
    elif function == 0:
        print("Bye now!")
        break