# input block 
sentence = input(("Enter the data : "))
sentence = sentence.lower()

for vowels in ['a','e','i','o','u']:  # Vowels 
# counter variable
    c = 0
    for word in sentence:
        if word == vowels:
            c += 1
    # only used vowels 
    if c != 0: 
        print(f"{vowels} \t {c}")