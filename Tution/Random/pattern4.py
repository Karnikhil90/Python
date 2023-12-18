num = 5 *2
for i in range (1,num+1,2):
    for k in range(1,num+1-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print()

for i in range (num,0,-2):
    for k in range(num-i,0,-1):
        print(" ",end="")
    for j in range(i,0,-1):
        print("*",end="")
    print()
