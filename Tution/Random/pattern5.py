n = 10 
for i in range(1,n+1,2):
    for blanks in range(1,n+1-i):
        print(" ",end="")
    for alpha in range(1,i+1):
        print("*",end=" ")
    print()