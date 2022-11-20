team = {"John": "software developer", "Ann": "project manager", "Susan": "software developer", "Jill": "lead developer"}

for value in sorted(set(team.values())):
    print(value)