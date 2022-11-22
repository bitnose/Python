def insert_degree_program(db, degree):
    #should print the degree program name and " is already in the database" if the degree program name already exists in the dictionary.
    if db.get(degree):
        print(f"{degree} is already in the database")
    else:
        db[degree.upper()] = []


def insert_course(db, degree, course):

    if degree in db:

        if course in db[degree]:
            print(f"{course[0]} is already in the database")
        else:
            db[degree].append(course)

    else:
        print(f"Unknown degree program: {degree}")


def print_degree_program(db, degree):
    
    if degree in db: 
        
        text = "courses" if len(db[degree]) > 1 else "course"

        print(f"{degree} ({len(db[degree])} {text})")

        total_credits = 0
        for course in db[degree]:
            print(f"  {course[0]}, {course[1]} credits")
            total_credits += course[1]

        print(f"  Total credits: {total_credits}")
    else:
        print(f"Unknown degree program: {degree}")

def remove_course(db, degree, course_name):

    if degree in db:
        for course in db[degree]:
            if course[0] == course_name:
                db[degree].remove(course)
            else:
                print(f"Unknown course: {course_name}")
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
    print()
    remove_course(db, "ITBBA", "Python Programming")
    print_degree_program(db, "ITBBA")
    print()
    # Testing error handling
    insert_degree_program(db, "ITBBA") 
    insert_course(db, "ITBBA", ("Time Management", 3))
    print_degree_program(db, "LOBBY")
    remove_course(db, "COMPU", "Surfing")
    remove_course(db, "ITBBA", "Surfing")
    

main()

