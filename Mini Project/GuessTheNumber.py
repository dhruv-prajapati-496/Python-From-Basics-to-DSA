import random

randomNumber = random.randint(1,100)
userInput = int(input("Guess a Number from 1 to 100: "))
def guessTheNumber(randomNumber,userInput):
    if(userInput == randomNumber):
        print("You Won: ", randomNumber, "is the correct number.")
        return
    elif(userInput>100 or userInput < 0):
        userInput = int(input("Please Enter a Number between 1 and 100: "))
        guessTheNumber(randomNumber, userInput)
    elif(userInput>randomNumber):
        userInput = int(input("Guessed Number is Large, Try to guess again: "))
        guessTheNumber(randomNumber,userInput)
    elif(userInput<randomNumber):
            userInput = int(input("Guessed Number is small, Try to guess again: "))
            guessTheNumber(randomNumber,userInput)

guessTheNumber(randomNumber,userInput)