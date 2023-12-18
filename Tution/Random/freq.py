# input block 
user_input = input(("Enter the data : "))
user_input = user_input.lower()

for alpla in range(ord('a'),ord('z')+1):  # aplabetes or the characters
# counter variable
    c = 0
    character = chr(alpla) # current character
    for i in user_input:
        if i == character:
            c += 1
    # only use character 
    if c != 0: 
        print(f"{character} \t {c}")
