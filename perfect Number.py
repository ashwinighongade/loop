num=int(input('Enter the number'))
sum=0
i=1
temp=num
while i<num:
    if num%i==0:
        sum=sum+i
    i=i+1
if sum==temp:
    print("perfect no")
else: 
    ("not perfect no")
