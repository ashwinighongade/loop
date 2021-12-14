num=int(input("Enter the number :"))
i=1
sum=0
while num>0:
    rem=num%10
    sum=sum+(rem*i)
    i=i*2
    num=num//10
print(sum)

# num=int(input("Enter the number :"))
# i=1
# rem=0
# while num>0:
#     rem=(num%2)*i
#     num=num//2
#     i=i*10
#     i.reverse()
# print(i)


