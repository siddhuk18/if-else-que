year=int(input("enter the number"))
if year%100==0:
    if year%400==0:
        print("this year is leap year")
    else:
        print("enter year is not leap year")
else:
    if year%4==0:
        print("enter the is leap year")
    else:
        print("enter year is not a leap year")
