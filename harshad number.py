num=int(input("Enter the number :"))
sum=0
org=num
while num>0:
    sum=sum+num%10
    num=num//10
if org%sum==0:
    print("This is harshad Number")
else:
    print("This is not harshad number")