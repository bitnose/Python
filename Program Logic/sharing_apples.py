apples = int(input("How many apples? "))
children = int(input("How many children? "))

if children != 0:
    apple_child = apples // children
    leftovers = apples % children
else:
    apple_child = 0
    leftovers = apples

print(f"\nEach child will get {apple_child} apples.")
print(f"There will be {leftovers} leftover apples.")
