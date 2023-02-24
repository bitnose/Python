start_time = int(input("Enter start time: "))
length = int(input("Enter length: "))
wage = float(input("Enter wage: "))

ending_time = start_time + length
salary = 0

while ending_time > 24:
    ending_time -= 24

if length>8:
    overtime = (length-8)*wage*2
    salary = 8*wage + overtime
else:
    salary = length * wage

print(f"\nThe work shift ends at {ending_time}:00")
print(f"The earnings are {salary:.2f} euros")