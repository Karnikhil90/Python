# Finding the sum of each letter in the sentence 

sentence = "I am the wisest alive, for I know one thing and that is that I know nothing"
sumof = 0

for word in sentence:
    if not word.isspace():
        sumof += ord(word) # adding the value of each word
print(f'The Sum of Each digits is {sumof}')
