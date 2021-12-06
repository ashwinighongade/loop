# month=input("Enter the month")
# if month=="jan" or month=="mar" or month=="may" or month=="july" or month=="aug" or month=="oct" or month=="dec":
#     print("the days of the month is 31 days")
#     if month=="jan" or month=="feb" or month=="dec":
#         print("this is winter season")
# if month=="feb":
#     print("the days of the month is 28 days")
# if month=="april" or month=="june" or month=="sep" or month=="nov":
#     print("the days of the month is 30 days")
# if month=="june" or month=="july" or month=="aug":
#     print("this month is summer season")
# if month=="sep" or month=="oct" or month=="nov":
#     print("this is month autumn season")
# if month=="mar" or month=="april" or month=="may":
#     print("this month is spring season")        


month=input("Enter the month")
if month=="jan" or month=="mar" or month=="may" or month=="july" or month=="aug" or month=="oct" or month=="dec":
    print("the days of the month is 31 days") 
    if month=="dec" or month=="jan":
        print("this month is winter season")
    elif month=="mar" or month=="may":
        print("this month is spring season")
    elif month=="july" or month=="aug":
        print("this month is summer season")
    elif month=="oct":
        print("this month is  autumn")



