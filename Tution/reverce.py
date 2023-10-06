num = int(input("Enter: "))

s = "" # str becasue of my easy algorithm
r=0
while(num > 0):
    r = num % 10
    s += str(r)
    num//=10

print(f"here is your result : {s}")