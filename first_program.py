
z = int(input("Number? "))
print(True if z in (1, 2, 6, 11, 22) else False)

z = True if z in (1, 2, 6, 11, 22) else False


# Yksi on pienempi kuin kaksi
print(1 < 2 == True)  # false


#
print(True == 1 < 2)  # true

i = 0
while i < 10:
    print(i)
    i += 1

for i in range(6, 19, 3):
    print(i)

age = int("ten years")
