'''
author = Radek Pakosta
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',

         '''
At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',

         '''
The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
         ]

separatorX = 50 * '-'
print(separatorX)
inputUsername = input(
    'Welcome to the Text-Analyzer app ;) \nPlease enter your username: ')
while len(inputUsername) == 0 or inputUsername.startswith(' '):
    inputUsername = input('Please enter at least 1 letter or number: ')
inputPassword = input('Please enter your password: ')
while len(inputPassword) == 0 or inputPassword.startswith(' '):
    inputPassword = input('Please enter at least 1 letter or number: ')

userReg = {'bob': '123', 'ann': 'pass123',
           'mike': 'password123', 'liz': 'pass123'}

while inputUsername in userReg.keys():
    inputUsername = input(
        'This username is already exist, please pick up a new one: ')

while inputPassword in userReg.values():
    inputPassword = input(
        'This password is already exist, please enter a new one: ')

print('\nThank you for registration :)')

print(separatorX)
textOption = input(
    'Please choose a number (1-3) of the text which should be analyzed: ')
while len(textOption) == (
        0 or not textOption.isdecimal() or (textOption.isdecimal() and
                                            (int(textOption) >= 4 or
                                                int(textOption) < 1))):
    textOption = input(
        'Please choose a number (1-3) of the text which should be analyzed: ')

textOption = int(textOption)

textForStats = TEXTS[textOption - 1]

print(textForStats)

print(separatorX)

textForStatsList = textForStats.split()


counterWord = []
capLetter = []
upperWords = []
lowerWords = []
onlyNum = []

for word in textForStatsList:
    counterWord.append(word)
    if word.istitle():
        capLetter.append(word)
    elif word.isupper():
        upperWords.append(word)
    elif word.islower():
        lowerWords.append(word)
    elif word.isdecimal():
        onlyNum.append(word)


print('There are', len(counterWord), 'words in the selected text.')
print('There are', len(capLetter), 'titlecase words.')
print('There are', len(upperWords), 'uppercase words.')
print('There are', len(lowerWords), 'lowercase words.')
print('There are', len(onlyNum), 'numeric strings.')

print(separatorX)
print('Word chart:\n')

barChartFreq = {}

for word in counterWord:
    wordStrip = word.strip(',.')
    barChartFreq[(len(wordStrip))] = barChartFreq.setdefault(
        len(wordStrip), 0) + 1

col1Width = 2
barChartFreqSorted = sorted(barChartFreq)

for item in barChartFreqSorted:
    print(str(item).rjust(col1Width), '*' *
          barChartFreq[item], barChartFreq[item])

print(separatorX)

sumNumb = 0
for num in onlyNum:
    sumNumb += int(num)

print('Total sum of the numbers in this text:', float(sumNumb))
print(separatorX)
