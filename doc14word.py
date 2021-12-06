use=input("Enter the number")
i=0
n=use
while i<len(use):
    a=int(n)%10
    n=int(n)//10
    if a==1:
        print("one",end=" ")
    elif a==2:
        print("Two",end=" ")
    elif a==3:
        print("Three",end=" ")
    elif a==4:
        print("four",end=" ")
    elif a==5:
        print("Five",end=" ")
    elif a==6:
        print("six",end=" ")
    elif a==7:
        print("seven",end=" ")
    elif a==8:
        print("eingh",end=" ")
    elif a==9:
        print("nine",end=" ")
    elif a==0:
        print("zero",end=" ")
    i+=1




    


