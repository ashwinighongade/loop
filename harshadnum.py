num=int(input("Enter the number :"))
sum=0
rem=0
org=num
while num>0:
    rem=num%10
    sum=sum+rem
    num=num//10
if org%sum==0:
    print("this number is harshad number")
else:
    print("this number is not harshad number")