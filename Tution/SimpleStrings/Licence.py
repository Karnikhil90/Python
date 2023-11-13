
#Using a function only for use multiple times

def fun():
#input segment 
    gender = input("Enter Your Gender : ")
    age = int(input("Enter Your age : "))
#conditions 
    # male 
    if gender == 'm' or 'male':
        if age >= 20 and age <= 60:
            print("You are eligible for licence ")
        else:
            print("Your age isn't eligible for licence ")
    # female 
    elif gender == 'f' or 'female':
        if age >= 18 and age <= 50:
            print("You are eligible for licence ")
        else:
            print("Your age isn't eligible for licence ")
    # Exceptional cases 
    else:
        print("Sorry Please, Enter an Valid input")

# Calling the function 

fun()