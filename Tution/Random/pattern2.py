n = 5
for i in range(n,0,-1):
    for blank in range(n-i,0,-1):
        print(" ",end="")
    for char in range(i,0,-1):
        print("*",end="")
    print()
