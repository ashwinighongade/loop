# check the given number is strong number or not
    
num=int(input("Enter the number : "))
sum=0
tem=num
while tem>0:
    fac=1
    i=1
    rem=tem%10
    while i<=rem:
        fac=fac*i
        i=i+1
    sum=sum+fac
    tem=tem//10
if sum==num:
    print("This number is strong number")
else:
    print("This number is strong number")