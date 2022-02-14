# Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).


i=1500
while i<=2500:
    if i%5==0 and i%7==0:
        print("divisible")
    else:
        print("not")
    i=i+1
