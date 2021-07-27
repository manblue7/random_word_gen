import random
import pandas as pd
import json
import dictionary



letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print('Press any button to generate random letters, then the letters will be searched for words in the dictionary, press "q" to quit\n')
while True:
    inp = input('Numnber of letters: ')
    if inp.lower() == 'q':
        break
    elif inp.isalpha() == False and  inp != '' and int(inp) < 1000001:
        letterString = ''
        words = []
        for i in range(int(inp)):
            ran = random.randint(0, 25)
            letterString += letters[ran]
        print(letterString)
        print('Searching...')
        df = pd.DataFrame(dictionary.dict, index=[0])
        for word in df.columns:
            if word in letterString and len(word) > 3:
                print(word, end=', ')
                words.append(word)
        print('\nNumber of random words generated: ', len(words))
        print('Here is a random word from the list: ', words[random.randint(0, len(words) - 1)])
        continue
    else:
        continue