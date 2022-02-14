# Write a program to print the following series till n terms.
# 2 , 22 , 222 , 2222 _ _ _ _ _ n terms




# num=int(input("enter the munber :"))
# sum=0
# i=1
# while i<=num:
#     sum=(sum*10)+2
#     print(sum,end=" ")
#     i=i+1



num=int(input("Enter number terms :"))
s=0
sum1=0
# print("series are ",end=" ")
for i in range(0,num):
    s=(s*10+2)
    print(s,end=" ")
    # sum1=sum1+s
#print("series are ",end=" ")