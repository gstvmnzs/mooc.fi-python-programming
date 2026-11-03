# Write your solution here
num_students = int(input("How many students on the course? "))
group_size = int(input("Desired group size? "))

if num_students % group_size == 0:
    num_groups = num_students / group_size
else:
    num_groups = num_students // group_size + 1

print(f"Number of groups formed: {num_groups}")