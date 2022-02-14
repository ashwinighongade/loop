a=1
while a<=300:
    i=1
    count=0
    while i<=a:
        if a%i==0:
            count+=1
        i+=1
    if count==2:
        print(a)
    if a==11:
        break
    a=a+1
    