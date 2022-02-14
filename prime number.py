# Write a program to check whether a number is prime or not.


num=int(input("Enter the Number :"))
count=0
i=1
while i<=num:
    if num%i==0:
        count+=1
    i+=1
if count==2:
    print("This is Prime Number")
else:
    print("This is not Prime Number")