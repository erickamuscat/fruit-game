#INF300 - Programming in Python
#Erick Jane Muscat
#Final Project
import random
import time

fruits = ["mango", "orange", "pear", "banana", "grapes", "papaya", "pineapple", "cantelope", "lychee", "grapefruit"]
plants = ["rose", "daisy", "lilies", "tulip", "buttercup", "hydrangea", "lilacs", "dahlia", "marigold"]
startGame = True
category = ""
continueGame = "Y"
userGuesslist = []
userGuesses = []



name = input("Please enter your name: ")
print("Hi there", name.capitalize() + ".", "Let's play Hangman!")
time.sleep(1)
print("There are two categories to choose from...")
time.sleep(2)
print("Choose wisely!")
time.sleep(1)
while True:
    #Choosing the Secret word
    while True:
        if category.upper() == 'F':
            secretWord = random.choice(fruits)
            break
        elif category.upper() == 'P':
            secretWord = random.choice(plants)
            break
        else:
            category = input("Pick a category: F for Fruits or P for Plants; X to leave. ")

        if category.upper() == 'X':
            print("Sad to see you go :( Goodbye!")
            startGame = False
            break

    if startGame:
        wordList = list(secretWord)
        guesses = (len(secretWord) + 3)

        #Utility function to print User Guess List
        def printGuessedLetter():
            print("Your word is: " + ''.join(userGuesslist))

        #Adding blank lines to userGuesslist to create the blank secret word
        for n in wordList:
            userGuesslist.append('_')
        printGuessedLetter()

        print("Allowed tries:", guesses)


        #starting the game
        while True:

            print("Guess a letter:")
            letter = input()

            if letter in userGuesses:
                print("You already guessed this letter, try again.")

            else:
                guesses -= 1
                userGuesses.append(letter)
                if letter in wordList:
                    print("Great job!")
                    if guesses > 0:
                        print("You have", guesses, 'guesses left!')
                    for i in range(len(wordList)):
                        if letter == wordList[i]:
                            letterIndex = i
                            userGuesslist[letterIndex] = letter.upper()
                    printGuessedLetter()

                else:
                    print("Oh no! Try again")
                    if guesses > 0:
                        print("You have", guesses, 'guesses left!')
                    printGuessedLetter()


            #Win/loss logic for the game
            joinedList = ''.join(userGuesslist)
            if joinedList.upper() == secretWord.upper():
                print("Congratulations! You won :)")
                break
            elif guesses == 0:
                print("Aw, man! Too many guesses.")
                print("The word was: "+ secretWord.upper())
                break

        #Play again logic for the game
        continueGame = input("Do you want to play again? Y to continue, any other key to quit: ")
        if continueGame.upper() == 'Y':
            category = input("Please select category - F for Fruits or P for Plants: ")
            userGuesslist = []
            userGuesses = []
            startGame = True
        else:
            print("Thank You for playing Hangman with me. See you again next time!")
            break
    else:
        break
