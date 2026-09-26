# Write your solution here
def sum_of_positives(nums):
    total = 0
    for num in nums:
        if num <= 0:
            continue
        total += num
    return total 



if __name__ == "__main__":
    sum_of_positives([1, 2])