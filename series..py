# Write a program to add first n terms of the following series using a while loop :
# 1/1! + 1/2! + 1/3! + …….. + 1/n!


num=int(input("Enter the Number :"))
fac=1
sum=0
i=1
while i<num:
    fac=fac*i
    sum=sum+i/fac
    i+=1
print(sum)