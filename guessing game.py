# Write a Python program to guess a number between 1 to 9

i=1
while i<=3:
    num=int(input("Enter the number between 1 to 9 :"))
    if i==2:
        print("congras! your correct guess")
    else:
        print("worng guess")
    i=i+1