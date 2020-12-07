import random

hangManPics = [''' +---+
                       |
                       |
                       |
                      ===''',
               ''' +---+
                   0   |
                       |
                       |
                      ===''',
               ''' +---+
                   0   |
                   |   |
                       |
                      ===''',
               ''' +---+
                   0   |
                  /|   |
                       |
                      ===''',
               ''' +---+
                   0   |
                  /|\  |
                       |
                      ===''',
               ''' +---+
                   0   |
                  /|\  |
                  /    |
                      ===''',
               ''' +---+
                   0   |
                  /|\  |
                  / \  |
                      ===''']


def getRandomWord(wordlist):
    wordIndex = random.randint(0, len(wordlist)-1)
    return wordlist[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(hangManPics[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')  # ends the output with a <space>
    for letter in missedLetters:
        print(letter, end=' ')
    print()
    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            # blanks[i] = secretWord[i] # TypeError: 'str' object does not support item assignment
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end=' ')

    print()

def getGuess(alreadyGuessed):
    while True:
        print('Guess a letter')
        guess = input('My Guess is: ')
        guess = guess.lower()  # Lower case the string

        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose another one')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz-':
            print('please enter a LETTER')
        else:
            return guess

def playAgain():
    print('Play again? (yes or no)')
    return input().lower().startswith('y')

if __name__ == "__main__":
    words = ['ambivert', 'calcspar', 'deaness', 'entrete', 'gades', 'monkeydom', 'outclimbed', 'outdared', 'pistoleers', 'redbugs', 'snake-line', 'subrules', 'subtrends', 'torenia', 'unhides']
    print(words)
    print('H A N G M A N')
    missedLetters = ''
    correctLetters = ''
    secretWord = getRandomWord(words)
    gameIsDone = False

    while True:
        displayBoard(missedLetters, correctLetters, secretWord)

        guess = getGuess(missedLetters + correctLetters)

        if guess in secretWord:
            correctLetters = correctLetters + guess

            # check if win
            foundAllLetters = True
            for i in range(len(secretWord)):
                if secretWord[i] not in correctLetters:
                    foundAllLetters = False
                    break
            if foundAllLetters:
                print('Yes! The secret word is ' + secretWord)
                gameIsDone = True
        else:
            missedLetters = missedLetters + guess

            # check if lost
            if len(missedLetters) == len(hangManPics) - 1:
                displayBoard(missedLetters, correctLetters, secretWord)
                print('You are lose! The true word is ' + secretWord)
                gameIsDone = True

        if gameIsDone:
            if playAgain():
                missedLetters = ''
                correctLetters = ''
                secretWord = getRandomWord(words)
                gameIsDone = False
            else:
                break
























