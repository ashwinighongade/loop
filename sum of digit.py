# Write a program to find the sum of the digits of a number accepted from the user.

num=int(input("Enter the Number :"))
sum=0
# rem=0
while num>0:
    sum=sum+num%10
    num=num//10
print(sum)

