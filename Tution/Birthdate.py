current_day = 5
current_month = 10
current_year = 2023 #constant 


#Input segement 
birth_day = int(input("Enter day: "))
birth_month = int(input("Enter month in numbers : "))
birth_year = int(input("Enter year: "))    

class fun:
    def __init__(self):
        super().__init__()

    def countringDays(self,birth_day,birth_month,birth_year):
     global current_day
     global current_month
     global current_year
        
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
     print(f"Days = {day}, Months = {month}, Years = {years}")

fun = fun()
fun.countringDays(birth_day,birth_month,birth_year)
