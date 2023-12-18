def length(data):
    data = str(input("Enter: "))
    print(f"Length is {len(data)}")

def length2(data):
    var =""
    x = ""
    for i in data:
        var = i + var
        x = var
        print(x,end="")
        var =""

length2("niku")