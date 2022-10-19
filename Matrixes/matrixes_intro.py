# Create two dimensional array/matrix and print elements
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(a[1])
print(a[2][2])

# Loop through two dimensional array
teams = [["Sue", "John"], ["Ann", "Susan"], ["Bo", "Dan", "Jo"]] 
for team in teams:
    print(*team, sep=", ")

# Check memoryplace 
a = ["A", "A", "A", "B"]
for item in a:
    print(id(item))