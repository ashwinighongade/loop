# 
# Write a program to print the sum of the first 10 Even numbers.


sum=0
i=1
while i<=20:
    if i%2==0:
        sum=sum+i
        print(sum)
    i+=1