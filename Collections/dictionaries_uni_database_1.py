def insert_degree_program(db, degree):
    #should print the degree program name and " is already in the database" if the degree program name already exists in the dictionary.
    if db.get(degree):
        print(f"{degree} is already in the database")
    else:
        db[degree.upper()] = []


def insert_course(db, degree, course):

    if degree in db:

        if course[0] in db[degree]:
            print(f"{course[0]} is already in the database")
        else:
            db[degree].append(course)

    else:
        print(f"Unknown degree program: {degree}")


def print_degree_program(db, degree):
    
    if degree in db: 
        
        print(f"{degree} ({len(db[degree])} courses)")

        total_credits = 0
        for course in db[degree]:
            print(f"  {course[0]}, {course[1]} credits")
            total_credits += course[1]

        print(f"  Total credits: {total_credits}")
    else:
        print(f"Unknown degree program: {degree}")
        
def main():
    db = {}
    insert_degree_program(db, "ITBBA")
    insert_degree_program(db, "EXPER")
    insert_course(db, "ITBBA", ("Python Programming", 5))
    insert_course(db, "ITBBA", ("Time Management", 3))
    insert_course(db, "EXPER", ("Creative Hospitality and Tourism", 5)) 
    insert_course(db, "EXPER", ("Managing Dynamic Restaurant Business", 10))
    print_degree_program(db, "ITBBA")
    print_degree_program(db, "EXPER")
main()
