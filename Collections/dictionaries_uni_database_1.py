def insert_degree_program(db, degree):
    #should print the degree program name and " is already in the database" if the degree program name already exists in the dictionary.
    if db.get(degree):
        print(f"{degree} is already in the database")
    else:
        db[degree.upper()] = {}


def insert_course(db, degree, course):

    if db.get(degree) != None:
        print(db[degree])

        if db[degree].get(course[0]) != None:
            print(f"{course[0]} is already in the database")
        else:
            db[degree][] = {"name": course[0], "credits": course[1]}
    else:
        print(f"Unknown degree program: {degree}")

    print("database", db)



def print_degree_program(db, degree):
    
    if db.get(degree): 
        print(f"{db[degree]} ({len(db[degree])} courses)")

        for course in list(db.values()):
            print(f"\n{db[degree][course]}, ({db[degree][credits]} courses)")

    else:
        print(f"Unknown degree program: {degree}")
        



def main():
    db = {}
    insert_degree_program(db, "ITBBA")
    insert_degree_program(db, "EXPER")
    insert_course(db, "ITBBA", ("Python Programming", 5))
    insert_course(db, "ITBBA", ("Time Management", 3))
   # insert_course(db, "EXPER", ("Creative Hospitality and Tourism", 5)) 
   # insert_course(db, "EXPER", ("Managing Dynamic Restaurant Business", 10))
   # print_degree_program(db, "ITBBA")
   # print_degree_program(db, "EXPER")
main()
