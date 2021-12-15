# num=int(iput("Enter the number :"))
# sum=0
# i=1
# while i<=10:
#     if i%2==0:
#         sum=sum+i
#         avr=sum/5
#     else:
#         sum=sum+i
#         avr_1=sum/5
#     i=i+1
# print(avr)
# print(avr_1)


# word=input("Enter the word :")
# print(word+"ing")


num=int(input("Enter the number :"))
if num>0:
    rem=(num%10)*10
    digit=num//10
    # print(rem)
    if digit>0:
        rem1=((digit%10)+rem)*10
        digit1=digit//10
        # print(rem1)
        if digit1>0:
            rem2=(digit1%10)+rem1
            print(rem2)

# word=input("Enter the word :")
# if 3==len(word):
#     print(word+"ing")
#     if 6==len(word):
#         print(word,+ly)
#     else:
#         ("wrong word")
# else:
#     ("wrong word")


    

