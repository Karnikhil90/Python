# isAmstrong number or not
# step 1 find out the length == power 
# step 2 not cut out the each number and give the power what just u find out

# 371 = 3^3  7^3  1^3  expample

# 1634 = 1 ^ length of the number  + 6 ^ length of the number + 3 ^ length of the number + 4 ^length of the number 

def doInput() -> int:
    user_input = int(input("Enter a number: "))
    return user_input

def isAmstrong(user_input) -> int:
    keep_Orginal = user_input
    
    length = len(str(user_input)) # convert the int to str, Because "len()" support str only 
    
    sumof = 0
    temp = 0
    while (user_input > 0):
        temp = user_input % 10 # last digit
        sumof += temp**length
        user_input //= 10 # cut last digit

    if keep_Orginal == sumof: 
        return True
    return False

if isAmstrong(doInput()):
    print("Its a amstrong number")
else:
    print("It's not a amstrong number")

