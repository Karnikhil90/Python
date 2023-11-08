from datetime import datetime 

time = datetime.now()

current_day,current_month,current_year = datetime.now().day,datetime.now().month,datetime.now().year

    #Input segement 
birth_day = int(input("Enter day: "))
birth_month = int(input("Enter month in numbers : "))
birth_year = int(input("Enter year: "))

# Conditions

if current_day < birth_day: #if current day is less than birth day
    day = (current_day + 30) - birth_day
    current_month -= 1
else:
    day = current_day - birth_day

if current_month < birth_month: #if current month is less than birth month
    month = (current_month + 12) - birth_month
    current_year -= 1
else:
    month = current_month - birth_month

years = current_year - birth_year

print("Days = {}, Months = {}, Years = {}".format(day, month, years))
