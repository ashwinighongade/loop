num=int(input("Enter the number :"))
amr=num
sum=0
while num>0:
    sum=sum+(num%10)*(num%10)*(num%10)
    num=num//10
if sum==amr:
    print("This number is armstrong number")
else:
    print("This number is not armstron number")



