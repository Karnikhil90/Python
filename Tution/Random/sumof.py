num = 456 # the data we will play 
# variable need as per the algorithm 
r=0
s=0
while(num > 0): # loop will work until the "num" become zero 
    r = num % 10 # taking the last digit
    s += r 
    num //= 10  # remove the last digit
print(f"The sum of 3 digit number is : {s}")

