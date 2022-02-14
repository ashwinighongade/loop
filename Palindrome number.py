# Write a program to check whether a number is palindrome or not.

num=int(input("Enter the number :"))
org=num
rev=0
while num>0:
    rev=(rev*10)+(num%10)
    num=num//10
# print(rev)
if rev==org:
    print("This is palindrome number")
else:
    print("This is not palindrome number")