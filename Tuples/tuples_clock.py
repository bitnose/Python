

def roll_forward(time, hours, minutes):
    
    hour, min = time
    min += minutes
    hour += hours

    full_hours = min// 60
    remaining_min = min % 60
    
    clock_hours = (hour + full_hours) // 24
    remaining_hours = (hour + full_hours) % 24
    return (remaining_hours, remaining_min)



def print_time(time):

    hours, min = time
    str_hours =  str(hours) if hours>10 else "0" + str(+hours)
    str_min =  str(min) if min>10 else "0" + str(+min)
    print(f"{str_hours}:{str_min}")
    


def main():

    time = (0,0)
    print(f"The current time is {time[0]}0:{time[1]}0")
    hours = int(input("Enter hours to add: "))

    while hours >= 0:
        minutes = int(input("Enter minutes to add: "))
        if minutes < 0:
            break
        time = roll_forward(time, hours, minutes)
        print_time(time)
        hours = int(input("Enter hours to add: "))   
             
if __name__ == "__main__":
    main()