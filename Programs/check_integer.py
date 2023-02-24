x = input("Enter an integer: ")

if len(x.strip()) == 0:
    print("\nNo input")

else:  
    try:
        x = int(x)
        even_count = 0
    
        for digit in str(x):
            if int(digit) % 2 == 0:
                even_count += 1

        print(f"\n{len(str(x))} digit(s)")
        print(f"{len(str(x))-even_count} odd digit(s)")
        print(f"{even_count} even digit(s)")

    except ValueError:
        print(f"\n\'{x}\' is not an integer")






