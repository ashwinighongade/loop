# i=1
# count=0
# num=int(input("Enter the number :"))
# while i<=num:
#     if num%i==0:
#         count=count+1
#     # print(count)
#     i=i+1
# if count==2:
#     print(num,"is prime number")
# else:
#     print(num,"is not prime number")


# num=int(input("enter the number :"))
# i=1
# count=0
# while(i<=num):
#     if num%i==0:
#         count=count+1
#     i=i+1
# if count==2:
#     print("parime")
# else:
#     print("no")

num=int(input("Enter the number :"))
i=1
while i<=num:
    if num==2 or num==3 or num==5 or num==7:
        print("prime no")
        i=i+1
        break
    if num%2!=0 or num%3!=0 or num%5!=0 or num%7!=0:
        print("prime no")
        i=i+1
        break
    else:
        print("not prime no")
        i=i+1
        break
    






