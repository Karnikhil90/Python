num = int(input("Enter the number : "))
org = num 
r = 0 # the last data or the sum of all the factors
s = 1
while num > 0:
    for i in range(1,(num % 10)+1):
        s *= i

    num //=10
    r += s
    s = 1

if r == org :
    print("Its a special number ")
else:
    print("Its not a special number ")