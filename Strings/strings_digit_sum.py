input = str(input("Enter a string: "))
nums = 0

for a in input:
    if a.isdigit():
        nums += int(a)
print(f"The sum of digits is {nums}")