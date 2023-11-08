# Geting a sentence and found
# the Number of Uppercase, Alphabtes and Symobls

sentence = "My name is @Nikhil"
sentence = sentence.strip()
# list_sentence = sentence.split()

print(f"The length of the input is {len(sentence)}")

# Counter Variable
upperCounter, numberCounter ,specilaCounter,alphaCounter=0,0,0,0

for word in sentence:
    if word.isalpha():
        if word.isupper():
            print(f'The {word} is UpperCase')
            upperCounter += 1
            alphaCounter += 1
        else:
            print(f'The {word} is alphabet')
            alphaCounter += 1                  
    elif word.isdigit():
        print(f'The {word} is Number:')
        numberCounter += 1
    else:
        if not word.isspace():
            print(f'The {word} is Symbol')
            specilaCounter += 1
    
           
print("\n====================================================\n")
print(f"Number of Alphabets is :{alphaCounter:^38}")
print(f"Number of number is :{numberCounter:^43}")
print(f"Number of Uppercase letter is :{upperCounter:^23}")
print(f"Number of SpecialCharacter letter is :{specilaCounter:^10}")

