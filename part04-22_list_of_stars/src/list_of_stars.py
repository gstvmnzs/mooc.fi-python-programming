# Write your solution here
def list_of_stars(list_of_int):
    for item in list_of_int:
        print("*" * item)

if __name__ == "__main__":
    numbers = [3, 7, 1, 1, 2]
    list_of_stars(numbers)