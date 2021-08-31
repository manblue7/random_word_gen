import random
from tkinter.constants import CENTER
import dictionary
import PySimpleGUI as sg




letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

layout = [[sg.Spin(values=[x for x in range(1, 100)], initial_value=1, key='num')],
[sg.Button('Generate', key='Gen')],
[sg.Text(text='', size=(10, 1), justification=CENTER, key='textbox', enable_events=True)],
[sg.Text(text='Words will appear here', key='words', size=(50, 20))]]
window = sg.Window('Random Word Generator', layout, size=(400, 300))
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Gen' and int(values['num'] < 100):
        numWords = int(values['num'])
        letterString = ''
        words = []
        for i in range(100000):
            ran = random.randint(0, 25)
            letterString += letters[ran]
        print(letterString)
        print('Searching.....')
        displayedWords = []
        for word in dictionary.dict:
            if word in letterString and len(word) > 3:
                words.append(word)
                print(word, end=', ')
        for word in range(numWords):
            displayedWords.append(words[random.randint(0, len(words))])
        print('\nNumber of random words generated: {}'.format(len(words)))
        window['words'].update(displayedWords)

