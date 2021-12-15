num=int(input("Enter the strat number :"))
num1= int (input("Enter the end number :"))
count=0
sum=0
sum1=0
count1=0
while num<=num1:
    if num%2==0:
        sum=sum+num
        count=count+1
        arv=sum/count
    if num%2!=0:
        sum1=sum1+num
        count1=count1+1
        arv1=sum1/count1
    num=num+1
print(sum)
print(arv)
print(sum1)
print(arv1)
