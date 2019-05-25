print("\nThis is the Number of Days Until Christmas Calculator!")

ly = input("\nIs it a leap year (y or n)?: ")
month = int(input("What is the month (as a number)?: "))
date = int(input("What is the date?: "))


if ly == "y" and month == 1 and date in range(1, 32):
    duc = 360 - date
elif ly == "n" and month == 1 and date in range(1, 32):
    duc = 359 - date

elif ly == "y" and month == 2 and date in range(1, 30):
    duc = 329 - date
elif ly == "n" and month == 2 and date in range(1, 29):
    duc = 328 - date

elif month == 3 and date in range(1, 32):
    duc = 300 - date

elif month == 4 and date in range(1, 31):
    duc = 269 - date

elif month == 5 and date in range(1, 32):
    duc = 239 - date

elif month == 6 and date in range(1, 31):
    duc = 208 - date

elif month == 7 and date in range(1, 32):
    duc = 178 - date

elif month == 8 and date in range(1, 32):
    duc = 147 - date

elif month == 9 and date in range(1, 31):
    duc = 116 - date

elif month == 10 and date in range(1, 32):
    duc = 86 - date

elif month == 11 and date in range(1, 31):
    duc = 55 - date

elif month == 12 and date in range(1, 26):
    duc = 25 - date
elif ly == "y" and month == 12 and date in range(26, 32):
    duc = 366 - (date - 25)
elif ly == "n" and month == 12 and date in range(26, 32):
    duc = 365 - (date - 25)

else:
    duc = "[Error]"


print("\nIt is only", duc, "days until Christmas!")


if month == 1 and date == 1:
    print("\nIt's New Years Day!  Have you thought of your new years revolutions yet?  Have a great new year!")

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

elif duc == "[Error]":
    print("\n**Something you entered was incorrect!  Please try again and read the instructions carefully.**")


print("\n[Coded, edited and updated by Fin McGhie]\n")
