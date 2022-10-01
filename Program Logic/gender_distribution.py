female = int(input("Enter the number of female students: "))
male = int(input("Enter the number of male students: "))

try:
    total = male + female
    female_percent = female / total * 100
    male_percent = male / total * 100
except ZeroDivisionError:
    female_percent = 0
    male_percent = 0

print(f"\nFemale: {female_percent:.1f} %")
print(f"Male: {male_percent:.1f} %")
