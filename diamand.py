# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print(i,end=" ")
#         j=j+1
#     print()
#     i=i+1


# i=1
# while i<=5:
#     j=5-i
#     while j>0:
#         print(" ",end="")
#         j=j-1
#     s=1
#     while s<=i:
#         print("*",end=" ")
#         s=s+1
#     print()
#     i=i+1
# i=4
# while i>=1:
#     j=5-i
#     while j>0:
#         print(" ",end="")
#         j=j-1
#     s=1
#     while s<=i:
#         print("*",end=" ")
#         s=s+1
#     print()
#     i=i-1


# word=input("Enter the word :")
# length=len(word)
# i=1
# vowel_count=0
# while i<=length:
#     if word=="a" or word=="i" or word=="o" or word=="e" or word=="u":
#         vowel_count+=1
# print(vowel_count)
# print(length)

length=int(input("enter the length :"))
width=int(input("Enter the width :"))
i=0
while i<=width-1:
    j=1
    while j<=length:
        if i==1  or width==width or length==length:
            print("*",end=" ")
        else:
            print(" ",end="")
        j=j+1
    print()
    i=i+1
    
    