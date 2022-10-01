weekday = input("Enter a weekday number: ")

try:
    valid = "OK" if int(weekday) in range(
        1, 8) else "Please enter an integer between 1 and 7"
    print(valid)

except ValueError:
    print("Please enter an integer between 1 and 7")
2
