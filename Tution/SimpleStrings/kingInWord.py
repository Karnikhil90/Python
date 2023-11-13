# Get a sentence and found the biggest word of the sentence 

sentence = 'We suffer more often in imagination than in reality'

new_sentence = sentence.split()

#TheBigWordInSentence im terms of ASCII CODES
StoreBigWord = ''
bigWord = 0
for word in new_sentence:
    #counter Variable
    TempCounter = 0
    for alpha in word:
        if not word.isspace():
            TempCounter += ord(alpha)
    if bigWord < TempCounter:
        # print("Debug: condition Items")
        bigWord = TempCounter
        StoreBigWord = word
        
print(f"The Biggest Word in terms of ASCII code is '{StoreBigWord}'")