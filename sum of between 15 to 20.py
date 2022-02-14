# Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.


i=1
sum=0
while i<=2:
    num=int(input("Enter the number"))
    sum=sum+num
    i=i+1
if sum>=15 and sum<=20:
    print("20")
else:
    print(sum)
