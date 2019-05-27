# calculates the number of days until christmas

def setup():
    global days_in_month, leap_year, feb_days, no_days_before, month, date, days_until, days_in_year
    print("\nThis is the Number of Days Until Christmas Calculator!")
   
    no_days_before = 0
    days_until = 0

    # gets inputs for the date
    leap_year = input("\nIs it a leap year (y or n)? ")
    month = int(input("What is the month (as a number)? "))
    # input validation
    while month < 1 or month > 12:
        print("Please enter a number between 1 and 12.")
        month = int(input("What is the month (as a number)? "))
    
    # if it is a leap year, then the number of days is set 
    if leap_year in ["y","Y","yes","Yes","YES"]:
        feb_days = 29
        days_in_year = 366
        if month == 1:
            no_days_before = 360
        elif month == 2:
            no_days_before = 329
    else:
        feb_days = 28
        days_in_year= 365
        if month == 1:
            no_days_before = 359
        elif month == 2:
            no_days_before = 328

    # sets up an array for the days in each month
    days_in_month = [31, feb_days, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    date = int(input("What is the date? "))
    while date < 1 or date > days_in_month[month - 1]:
        print("Please enter a number between 1 and the number of days in the month.")
        date = int(input("What is the date? "))
    
    # sets up the number of days for each month
    #for loop in range(3,11):
    #    if month == (loop+1):
    #        no_days_before = days_in_year - days_in_month[loop]

    if month == 3:
        no_days_before = 300
    elif month == 4:
        no_days_before = 269
    elif month == 5:
        no_days_before = 239
    elif month == 6:
        no_days_before = 208
    elif month == 7:
        no_days_before = 178
    elif month == 8:
        no_days_before = 147
    elif month == 9:
        no_days_before = 116
    elif month == 10:
        no_days_before = 86
    elif month == 11:
        no_days_before = 55

    # no_days_before for the days after christmas
    if month == 12 and date in range(1, 26):
        no_days_before = 25 + date
    elif month == 12 and date in range(26, 32): 
        no_days_before = days_in_year + (date + 25)



def find_days_until():
    global days_until

    for loop in range(1, 12):
        days_until = no_days_before - date
        if month == 12 and date in range(1, 26):
            days_until = 25 - date
        elif month == 12 and date in range(26, 32):
            days_until = days_in_year - (date - 25)


def message():
    print("\nIt is only", days_until, "days until Christmas!")

    if month == 1 and date == 1:
        print("\nIt's New Years Day!  Have you thought of your new years resolutions yet?  Have a great new year!")

    elif month == 3 and date == 23:
        print("\nIt's Katie's birthday today!  Happy birthday Katie and have an amazing day!")

    elif month == 4 and date == 3:
        print("\nIt's Fin's birthday today!  Happy birthday Fin and have an amazing day!")

    elif month == 5 and date == 5:
        print("\nIt's Dad's (Gus's) birthday today!  Happy birthday Dad (Gus) and have an amazing day!")

    elif month == 5 and date == 12:
        print("\nIt's Tara's birthday today!  Happy birthday Tara and have an amazing day!")

    elif month == 11 and date == 5:
        print("\nIt's Mum's (Di's) birthday today!  Happy birthday Mum (Di) and have an amazing day!")

    elif month == 12 and date == 24:
        print("\nWOW!!!  It's Christmas eve today!  (Which means it's Christmas tomorrow!)")

    elif month == 12 and date == 25:
        print("\nOMG!!!  IT'S CHRISTMAS TODAY!!!  HO HO HO!  \nMerry Christmas!")

    elif month == 12 and date == 26:
        print("\nIt's Boxing Day today!  I hope you enjoyed Christmas yesterday!  Have a great day!")

    elif month == 12 and date == 31:
        print("\nIt's Hogmany today!  Have a great last day of the year!")



# main program
setup()
find_days_until()
message()
print("\n[Coded, edited and updated by Fin-M]")
print("[Updated by Kingdunnad (Daisy)]")