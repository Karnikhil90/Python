# getting both of the word
first_Word = input('Gimme a word: ')
sencond_Word = input('Gimme another word : ')

sumFirst,sumSecond= 0,0 #Will be store the value of each letter form the word

for word in first_Word: 
    sumFirst += ord(word)   # adding the value of each word

for word in sencond_Word:
    sumSecond += ord(word) # adding the value of each word

if sumFirst > sumSecond:
    print(f'The Greater Word is {first_Word} with {sumFirst}') 
else:
    print(f'The Greater Word is {sencond_Word} with {sumSecond}')