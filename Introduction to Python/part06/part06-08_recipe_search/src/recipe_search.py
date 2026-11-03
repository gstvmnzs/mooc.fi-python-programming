# Write your solution here
def recipe_as_list(filename: str):
    lines = []
    with open(filename) as recipe_book:
        for line in recipe_book:
            lines.append(line.strip())
    return lines
            
def search_by_name(filename: str, word: str):
    recipes = recipe_as_list(filename)
    
    found = []
    for i in range(len(recipes)):
        if i == 0 and word.lower() in recipes[i].lower():
            found.append(recipes[i])
        elif recipes[i] == "" and word.lower() in recipes[i+1].lower():
            found.append(recipes[i+1])
    return found

def search_by_time(filename: str, prep_time: int):
    recipes = recipe_as_list(filename)
    
    found = []
    for i in range(len(recipes)):
        if i > 0 and recipes[i] == "" and int(recipes[i+2]) <= prep_time:
            found.append(f"{recipes[i+1]}, preparation time {recipes[i+2]} min")
        elif i == 0 and int(recipes[i+1]) <= prep_time:
            found.append(f"{recipes[i]}, preparation time {recipes[i+1]} min")
    return found

def search_by_ingredient(filename: str, ingredient: str):
    recipes = recipe_as_list(filename)
    recipes_parts = []
    found = []
    
    for i in range(len(recipes)):
        if recipes[i] == "":
            for i in range(len(recipes_parts)):
                if i > 1 and ingredient in recipes_parts[i]:
                    found.append(f"{recipes_parts[0]}, preparation time {recipes_parts[1]} min")
                    break
            recipes_parts = []
        else:
            recipes_parts.append(recipes[i])
    for i in range(len(recipes_parts)):
        if i > 1 and ingredient in recipes_parts[i]:
            found.append(f"{recipes_parts[0]}, preparation time {recipes_parts[1]} min")
    return found