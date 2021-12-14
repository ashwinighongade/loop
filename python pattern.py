word=input("Enter the word :")
length=len(word)
for i in range(length):
    for j in range(i+1):
        print(word[i],end="")
    print()
    
