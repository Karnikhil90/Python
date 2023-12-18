#   *
#  * *
# * * *
#  * *
#   *


num = 5



for i in range (1,num+1):
    for k in range(1,num+1-i):
        print(" ",end="")
    for j in range (1,i+1):
        print("*",end="")
    print()



for i in range (num,0,-1):
    for k in range(num-i,0,-1):
        print(" ",end="")
    for j in range (i,0,-1):
        print("*",end="")
    print()







# for i in range (num-1,0,-1):
#     for j in range (1,i+1):
#         print("*",end="")
#     for k in range(6-i,1):
#         print(" ",end="")
#     print()
