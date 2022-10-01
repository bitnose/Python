letter = input("Enter grade letter: ")
letters = ["A", "A", "B", "A", "C", "B", "C", "F", "B", "B", "A", "A", "C", "C", "C"]
count = 0

for i in range(len(letters)):
    if letter == letters[i]:
        count = count + 1
       
percentage = len(letters)
print(f"{count/percentage*100:.2f} %")