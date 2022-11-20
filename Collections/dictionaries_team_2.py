team_members = {"John": "software developer", "Ann": "project manager", "Susan": "software developer", "Jill": "lead developer"}
for key in list(team_members.keys()):
    print(key, end=" ")

print()

for key in sorted(team_members.keys()):
    print(key, end=" ")