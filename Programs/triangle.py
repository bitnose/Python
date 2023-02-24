pos_integer = int(input("Enter positive integer: "))
to_string = str(pos_integer)

for i in range(1, pos_integer):
    print(to_string * i)

for i in range(pos_integer, 0, -1):
    print(to_string * i)
