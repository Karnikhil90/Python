# is Dark number or not 
# if any number conain "zero" then that is dark number 

def isDark(user_input) -> int:
    counter = -1
    while user_input > 0:
        temp = user_input % 10
        if temp == 0:
            counter += 1 
            break
        user_input //= 10
    return counter

def doInput() -> int:
    user_input = int(input("Enter a number: "))
    return user_input


if isDark(doInput()) == -1:
    print("This not a dark number")
else:
    print("This is a dark number")
