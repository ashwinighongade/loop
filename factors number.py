# Write a program to print all the factors of a number using a while loop .

num=int(input("Enter the Number :"))
i=1
while i<=num:
    if num%i==0:
        print(i)
    i+=1