# Write your solution here
def factorials(n: int):
    my_dict = {}
    
    for i in range(1, n + 1):
        my_dict[i] = 1
        for x in range (1, i+1):
            my_dict[i] *= x
    
    return my_dict

if __name__ == "__name__":
    k = factorials(1)
    print(k[1])