# Write a program to find the product of the digits of a number accepted from the user.

num=int(input("Enter the digit :"))
product=1
while num>0:
    product=product*(num%10)
    num=num//10
print(product)

