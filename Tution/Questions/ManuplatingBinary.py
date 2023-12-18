# Manuplating Binary 
# getting the number from 1 to 15 the print the binary(without inbuilt functions)
# print the original and the mirror image of binary.

#Git the input of number 

userInput_Name:int = int(input("Single letter only: "))
number:int = userInput_Name
# Process 
    # Binary Finding using LCM 
product = ""
while number > 0:
    temp = number % 2 # Getting the reminder of the product
    product += str(temp) #Andding 
    number //= 2 #Removing 


# Output 
    # The Input letter , original binary and mirror image
print(f"{userInput_Name} : Binary {product[::-1]} Mirror {product}")