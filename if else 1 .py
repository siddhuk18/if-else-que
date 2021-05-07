num=int(input("enter the number"))
num_1=int(input("enter the number"))
operator=input("enter the symbol")
if operator=="+":
    a=(num+num_1)
    print(a)
elif operator=="-":
    a=(num-num_1)
    print(a)
elif operator=="*":
    a=(num*num)
    print(a)
elif operator=="/":
    a=(num/num_1)
    print(a)
i=1
while i<=a:
    print(i)
    i=i+1