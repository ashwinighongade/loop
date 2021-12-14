num=int(input("Enter the number"))
sum=0
tem=num
while tem>0:
    fac=1
    i=1
    rem=tem%10
    # print(rem,"remmm")
    while i<=rem:
        fac=fac*i
        i=i+1
    sum=sum+fac
    tem=tem//10

if sum==num:
    print("this is strong number")
else:
    print("this is not strong number")   
    

