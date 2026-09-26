# Write your solution here
def distinct_numbers(nums):
    new = []
    for item in nums:
        if item not in new:
            new.append(item)
    new.sort()
    return new