# num=int(input("enter the munber :"))
# sum=0
# i=1
# while i<=num:
#     sum=(sum*10)+num
#     print(sum,end=" ")
#     i=i+1

# str="computer"
# i=0
# while i< len(str):
#     print(str[i])
#     i=i+1

# word=input("Enter the word :")
# i=1
# while i<=len(word):
#     j=1
#     while j<=i:
#         print(j,end="")
#         j=j+1
#     print()
#     i=i+1

string=input("Enter the word :")
length=len(string)
for i in range(length):
    for j in range(i+1):
        print(string[j],end="")
    print()