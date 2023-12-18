# is palindrom
sentence = 'I love my mom and dad'
nw_sentence = sentence.split()
for word in nw_sentence:
    if len(word) != 1:
        if word.lower() == word[::-1].lower():
            print(word)