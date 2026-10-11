# Write your solution here
def oldest_person(people: list):
    min_year = people[0][1]
    oldest = people[0][0]
    
    for person in people:
        if person[1] < min_year:
            min_year = person[1]
            oldest = person[0]
    
    return oldest
            