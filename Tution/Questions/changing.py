# main = [8,10,15,3,6] I have to change 
# but take a input in a variable that how much I want to shift 
# For now take a example of 2 input in the variables
# Then it will change the main into [3,6,8,10,15]


main = [8,10,15,3,6]
inpSteps = int(input("Enter how many steps u want :"))
if inpSteps > 0:
    getSteps = len(main) - inpSteps
else:
    print("Give a Postive Input, Its a Error!")

newMain = []
newMain = main[getSteps : ] + main[:getSteps]
print(newMain)