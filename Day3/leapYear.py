"""
Leap Year Calculation
on every year that is evenly divisible by 4
except every year that is evenly divisible by 100
unless the year is also evenly divisible by 400.
"""

year = int(input("Which year do you want to check? "))
leapYear = False

if year % 4 == 0:
    leapYear = True
    if year % 100 == 0:
        leapYear = False
        if year % 400 == 0:
            leapYear = True

if leapYear :
    print(f"Year {year} is a leap year.")
else :
    print(f"Year {year} is not a leap year.")