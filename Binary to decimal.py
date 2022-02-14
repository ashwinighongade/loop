# Write a program to convert binary to decimal.
num=int(input("Enter the number :"))
i=1
sum=0
while num>0:
    rem=num%10
    sum=sum+(rem*i)
    i=i*2
    num=num//10
print(sum)