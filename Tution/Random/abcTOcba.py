def fun1():
    a = 1
    b = 2
    c = 3
    print("After setting the value: ") 
    print("the a = {},b = {},c = {}".format(a,b,c))
    #swap
    a = a + b + c
    b = a-(b+c)
    c = a-(b+c)
    a = a-(b+c)

    print("After swap the value : ")
    print("the a = {},b = {},c = {}".format(a,b,c))

def fun2():
    a = 1 
    b = 2
    c = 3
    print("Before setting the value: ") 
    print("the a = {},b = {},c = {}".format(a,b,c))
    #swap 
    d = c
    c = b
    b = a 
    a = d
    print("After setting the value: ") 
    print("the a = {},b = {},c = {}".format(a,b,c))
    
def fun3():
    a = 1
    b = 2 
    c = 0
    print("Before change ")
    print("The a {}  and the b {}".format(a,b))
    a = a + b
    b = a - b
    a = a - b
    print("After the change ")
    print("The a {}  and the b {}".format(a,b))
    
fun1()
#calling the function 
