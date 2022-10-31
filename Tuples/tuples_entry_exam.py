def grade_exam(applicants, score):

    passed_applicants = []
    for applicant in applicants:
        if applicant[1] >= score:
            passed_applicants.append(applicant)
    
    return passed_applicants

def main():
    applicants = [("Ann", 30), ("Jack", 25), ("Jill", 40)]
    passed_applicants = grade_exam(applicants, 30) 
    print("Entry exam passed")
    
    for name, points in passed_applicants:
        print(f"{name}, {points} points")

if __name__ == "__main__":
    main()