# Write your solution here
def dict_of_numbers():
    new_dict = {}
    small_nums = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen"
    }
    tens = {
        2: "twenty",
        3: "thirty",
        4: "forty",
        5: "fifty",
        6: "sixty",
        7: "seventy",
        8: "eighty",
        9: "ninety"
    }
    
    for i in range (100):
        if i in small_nums:
            new_dict[i] = small_nums[i]
        else:
            unit = i % 10
            ten = i // 10
            if unit != 0:
                new_dict[i] = f"{tens[ten]}-{small_nums[unit]}"
            else:
                new_dict[i] = f"{tens[ten]}"
    return new_dict