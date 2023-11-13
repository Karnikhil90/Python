# In the Sentence only The word start with "S" and "T" will be printed 

sentence = "Always Say less Then necessary"
new_sentence = sentence.split()

for word in new_sentence:
    if (word[0].lower()) == 's'or (word[0].lower()) == 't':
        print(word)