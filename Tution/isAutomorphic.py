num = 8
temp =num

lenght = len(str(num))
r =0
s =""
for i in range(1,lenght+1):
    r = (num**2) % 10
    s = str(r) + s

if temp ==int(s):
    print("Its a ")
else:
    print("Is not")