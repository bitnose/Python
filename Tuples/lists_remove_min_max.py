def remove_min_max(a):

    if len(a) > 0:
        a.remove(min(a))
        if len(a) >0:
            a.remove(max(a)) 
        
        

def main():
    a = [1,3,5] 
    remove_min_max(a) 
    print(a)

if __name__ == "__main__":
    main()