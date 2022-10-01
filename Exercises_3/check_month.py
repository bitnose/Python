month = input("Enter a month number: ")
isMonth = False

while isMonth == False:
    try:
        if int(month) in range(1, 13):
            print("OK")
            isMonth = True
        else:
            print(f"{month} is not a valid month number")
            month = input("\nEnter a month number: ")
    except ValueError:
        print(f"'{month}' is not a valid month number")
        month = input("\nEnter a month number: ")
