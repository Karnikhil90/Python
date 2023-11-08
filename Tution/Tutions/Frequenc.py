# input block 
user_input = input(("Enter the data : "))
user_input = user_input.lower()

for alpla in range(ord('a'),ord('z')+1):  # aplabetes or the characters
# counter variable
    counter = 0
    character = chr(alpla) # current character
    for word in user_input:
        if word == character:
            counter += 1 
    # only use character 
    if counter != 0: 
        print(f"{character} \t {counter}")