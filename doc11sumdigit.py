num=int(input("Enter the digit :"))
sum=0
i=1
while num>0:
    sum=sum+num%10
    num=num//10
print(sum)
i=i+1



