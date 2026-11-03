# Write your solution here
def run(program):
    result = []
    variables = {
        "A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0, "K": 0, "L": 0, "M": 0,
        "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0, "U": 0, "V": 0, "W": 0, "X": 0, "Y": 0, "Z": 0
    }
    labels = {}
    
    label_index = 0
    for item in program:
        command = item.split()
        if ":" in command[0]:
            labels[command[0][:len(command[0])-1]] = label_index
        label_index += 1
    
    i = 0
    while i < len(program):
        command = program[i].split()
        
        if "MOV" in command:
            try:
                variables[command[1]] = int(command[2])
            except ValueError:
                variables[command[1]] = variables[command[2]]
        elif "PRINT" in command:
            if command[1] in variables:
                result.append(variables[command[1]])
            else:
                result.append(int(command[1]))
        elif "ADD" in command:
            try:
                variables[command[1]] += int(command[2])
            except ValueError:
                variables[command[1]] += variables[command[2]]   
        elif "SUB" in command:
            try:
                variables[command[1]] -= int(command[2])
            except ValueError:
                variables[command[1]] -= variables[command[2]]  
        elif "MUL" in command:
            try:
                variables[command[1]] *= int(command[2])
            except ValueError:
                variables[command[1]] *= variables[command[2]]  
        elif "END" in command:
            return result
        elif ":" in command[0]:
            pass
        elif "IF" in command:
            test = False
            
            if "==" in command:
                if command[3] in variables:
                    if variables[command[1]] == variables[command[3]]:
                        test = True
                else:
                    if variables[command[1]] == int(command[3]):
                        test = True

            elif "!=" in command:
                if command[3] in variables:
                    if variables[command[1]] != variables[command[3]]:
                        test = True
                else:
                    if variables[command[1]] != int(command[3]):
                        test = True
                        
            elif ">=" in command:
                if command[3] in variables:
                    if variables[command[1]] >= variables[command[3]]:
                        test = True
                else:
                    if variables[command[1]] >= int(command[3]):
                        test = True
                    
            elif "<=" in command:
                if command[3] in variables:
                    if variables[command[1]] <= variables[command[3]]:
                        test = True
                else:
                    if variables[command[1]] <= int(command[3]):
                        test = True
                    
            elif "<" in command:
                if command[3] in variables:
                    if variables[command[1]] < variables[command[3]]:
                        test = True
                else:
                    if variables[command[1]] < int(command[3]):
                        test = True
                    
            elif ">" in command:
                if command[3] in variables:
                    if variables[command[1]] > variables[command[3]]:
                        test = True
                else:
                    if variables[command[1]] > int(command[3]):
                        test = True
            
            if test:
                command = [command[4], command[5]]
                
        if "IF" not in command and "JUMP" in command:
            i = labels[command[1]] - 1
        
        i += 1
        
    return result