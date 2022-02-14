num=int(input("Enter the first number :"))
num_1=int(input("Enter the second number :"))
i=1
while (i<=num and i<=num_1):
    if num%i==0 and num_1%i==0:
        hcf=i
    i=i+1
print(hcf)


# # lcf
# num=int(input("Enter the first number :"))
# num_1=int(input("Enter the second number :"))
# maxNum=max(num, num_1)
# while(True):
#     if (maxNum%num==0 and maxNum%num_1==0):
#         break
# print(maxNum)
