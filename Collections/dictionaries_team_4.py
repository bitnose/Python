team = {"John": "software developer", "Ann": "project manager", "Susan": "software developer", "Jill": "lead developer"}

name = input("Enter name (quit ends): ")

while name!="quit":

    role = input("Enter role: ")
    team[name] = role.lower()

    name = input("\nEnter name (quit ends): ")

print()
for key, value in sorted(team.items()):
    print(f"{key:8s}{value:8s}")