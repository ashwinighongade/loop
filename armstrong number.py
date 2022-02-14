# Write a program to check whether a number is Armstrong or not. (Armstrong number is a number that is equal to the sum of cubes of its digits, for example : 153 = 1^3 + 5^3 + 3^3.)
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
