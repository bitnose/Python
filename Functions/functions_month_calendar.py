from cgitb import lookup
from datetime import date
from calendar import monthrange


def print_month_calendar(year: int, month: int):

    month_names = ["", "January", "February", "March", "April", "May", "June",
                   "July", "August", "September", "October", "November", "December"]

    month_name = month_names[month]
    my_date = date(year, month, 1)
    days_in_the_month = monthrange(my_date.year, my_date.month)[1]
    day_of_week = my_date.weekday() + 1

   # print(f"{day:4d}")

    print(f"\n> {month_name} {year} <")
    print(" Mon  Tue  Wed  Thu  Fri  Sat  Sun ")

    for i in range(1, days_in_the_month+1):
        print(f"{i:4d}", end=" ")


def main():
    try:
        year = int(input("Enter year: "))
        month = int(input("Enter month: "))
        calendar = print_month_calendar(year, month)
        print(calendar)
    except ValueError:
        print("Wrong value")


main()
