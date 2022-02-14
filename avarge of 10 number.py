# Write a program to accept 10 numbers from the user and display it’s average.
i=0
sum=0
while i<=10:
    num=int(input("Enter the number"))
    sum=sum+num
    i=i+1
    avarge=float(sum/10)
print("The sum of 10 number is",sum)
print("The avarge of 10 number",avarge)