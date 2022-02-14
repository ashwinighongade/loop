# Write a program to display the number names of the digits of if the number is 231 then output should be Two a number entered by user, for example Three One

num=input("Enter the number :")
i=0
while i<len(num):
    # print(num)
    if num[i]==str(1):
        print("One",end=" ")
    elif num[i]==str(2):
        print("Two",end=" ")
    elif num[i]==str(3):
        print("Three",end=" ")
    elif num[i]==str(4):
        print("Four",end=" ")
    elif num[i]==str(5):
        print("Five",end=" ")
    elif num[i]==str(6):
        print("Six",end=" ")
    elif num[i]==str(7):
        print("Seven",end=" ")
    elif num[i]==str(8):
        print("Eight",end=" ")
    elif num[i]==str(9):
        print("Nine",end=" ")
    elif num[i]==str(0):
        print("Zero",end=" ")
    i+=1

