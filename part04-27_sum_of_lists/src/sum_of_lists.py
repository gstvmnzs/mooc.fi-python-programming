# Write your solution here
def list_sum(int_list1, int_list2):
    new = []
    for i in range(len(int_list1)):
        result = 0
        result = int_list1[i] + int_list2[i]
        new.append(result)
    return new
        