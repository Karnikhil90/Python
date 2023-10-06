# input block 
user_input = input(("Enter the data : "))
user_input = user_input.lower()

for vowels in ['a','e','i','o','u']:  # Vowels or the characters
# counter variable
    c = 0
    character = chr(vowels) # current character
    for i in user_input:
        if i == character:
            c += 1
    # only use character 
    if c != 0: 
        print(f"{character} \t {c}")
