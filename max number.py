# find the maximum number given between 10 number

# i=1
# max=0
# while i<=10:
#     num=int(input("Enter the number :"))
#     if num>max:
#        max=num
#     i+=1
# print(max)

small=0
max=0
i=0
while i<10:
    num=int(input("Enter the number :"))
    if num>max:
        max=num
    else:
        small=num  
    i+=1
print(max)
print(small)    
