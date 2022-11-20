team = {"John": "software developer", "Ann": "project manager", "Susan": "software developer", "Jill": "lead developer"}

name = input("Enter name (quit ends): ")

while name!="quit":

    if team.get(name) != None:
        print(f"{name} is a {team[name]}")
    else:
        print(f"{name} is not in the team")

    name = input("Enter name (quit ends): ")
