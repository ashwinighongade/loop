# num=int(input("Enter the number"))
# rem=0
# org=num
# while num>0:
#     rem=(rem*10)+(num%10)
#     num=num//10
# if org==rem:
#     print("palindrome")

# num=int(input("enter the number :"))
# i=65
# while i<=(65+num):
#     j=65
#     while j<=i:
#         print(chr(i),end=" ")
#         j=j+1
#     print() 
#     i=i+1

# for i in range(65,71):
#     for j in range(65,i+1):
#         print(chr(j),end=" ")
#     print()
num=int(input("Enter the number :"))
i=66
while i<=(66+num):
    j=66
    while j<=(num-i):
        print(" ",end=" ")
        j=j+1
    n=66
    while n<=i:
        print(chr(j),end=" ")
        n=n+1
    print()
    i=i+1