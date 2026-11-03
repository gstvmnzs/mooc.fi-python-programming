# Write your solution here
def read_input(request:str, lower_bound:int, upper_bound:int):
    while True:
        try:
            user = int(input(request))
            if user <= upper_bound and user >= lower_bound:
                return user
        except ValueError:
            pass
        print(f"You must type in an integer between {lower_bound} and {upper_bound}")