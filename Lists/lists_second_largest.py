from re import A


def second_largest(a):
    try:
        sorted_set = sorted(set(a), reverse=True)
        return sorted_set[1]
    except: 
        return None
    

def main():
    a = [0, 0, -4, 0]
    b = [1]
    c = []
    print(second_largest(a))

if __name__ == "__main__":
    main()



#Create a program called lists_second_largest. 
#The program should have a function named second_largest that takes a list as argument. 
# The function should return a copy of the second largest value in the list.
#  If the list has no values, or if it has only one distinct value, the function should return None.