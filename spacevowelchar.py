# sentence=input("Enter the sentence :")
# length=len(sentence)
# space=sentence.count(" ")
# character=length-space
# # sentence_lower=sentence.lower(sentence)
# vowel="aeiou"
# vowel_count=0
# # con="bcdfghjklmnpqrstvwxyz"
# # con_count=0
# for i in sentence:
#     if i in vowel:
#         vowel_count+=1
#         print(i)
# print("length",length)
# print("Space",space)
# print("vowel count",vowel_count)
# print("character",character)

sentence=input("Enter the sentence :")
length=len(sentence)
space=sentence.count(" ")
character=length-space
sentence_lower=sentence.lower()
print(sentence_lower)
vowel="aeiou"
vowel_count=0
con_c=0
con="bcdfghjklmnpqrstvwxyz"
# con_count=0
for i in sentence:
    if i in vowel:
        vowel_count+=1
        # print(i)
    elif i in con:
        con_c+=1
print("length",length)
print("Space",space)
print("vowel count",vowel_count)
print("character",character)
print("consp",con_c)



# user=int(input("enter"))
# i=0
# while i<=user:
#     if i%2==0:
#         print(i,"even")
#     else:
#         print(i,"odd")
#     i+=1
