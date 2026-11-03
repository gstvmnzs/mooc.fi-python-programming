# Write your solution here
def find_words(search_term:str):
    with open("words.txt") as words:
        found = []
        for line in words:
            line = line.strip()
            
            if "." in search_term:
                if len(line) == len(search_term):
                    matches = True
                    for i in range(len(search_term)):
                        if search_term[i] != "." and search_term[i] != line[i]:
                            matches = False
                            break
                    if matches:
                        found.append(line)
            elif "*" in search_term:
                if search_term[len(search_term)-1] == "*":
                    if line.startswith(search_term[:len(search_term)-1]):
                        found.append(line)
                elif search_term[0] == "*":
                    if line.endswith(search_term[1:]):
                        found.append(line)
            else:
                if search_term == line:
                    found.append(line)
    return found