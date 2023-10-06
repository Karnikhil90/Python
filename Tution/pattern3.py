n = 5*2
for i in range(1,n+1,2):
    for k in range(1,n+1,i):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print()
