i=int(input("Enter the number :"))
product=1
while i>0:
    product=product*(i%10)
    i=i//10
    print(product)