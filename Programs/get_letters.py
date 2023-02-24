text = str(input("Enter a string: "))
new_text = []
print()

if text.isdigit():
    print("No letters")
elif text.strip() == "":
    print("No input")
else:
    for x in text:
        if x.isalpha():
            new_text.append(x.lower())
    print(*sorted(set(new_text)), sep=" ")
