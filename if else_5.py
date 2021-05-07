per=int(input("enter the number"))
    tax=15/100*per
elif per>50000 and per<=10000:
    tax=10/100*per
else:
    tax=5/100*per
    print("tax to be paid",tax)
    