# getting two string as a word 
# Then:
    # Print the comman letter and uncomman letter
FirstWord = input('Gimme a word not a sentence: ')
SecondWord = input('Gimme a word not a sentence: ')

FirstWord = FirstWord.strip()
SecondWord = SecondWord.strip()
 
# comman words 
print("="*20,'\nThe Comman words :')
for word in FirstWord:
    cheak = SecondWord.find(word)
    if cheak != -1:
        print(word)

# UnComman words
print("="*20,'\nThe UnComman words :')
for word in FirstWord:
    cheak = SecondWord.find(word)
    if cheak == -1:
        print(word)
