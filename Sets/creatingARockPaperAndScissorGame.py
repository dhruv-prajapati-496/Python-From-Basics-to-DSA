# Rock, Paper and Scissor Game
Set = {"rock","paper","scissor"}
value = Set.pop()
userInput = input("Enter (Rock, Paper, Scissor): ").lower();
if(userInput == value):
    print("Draw")
elif(userInput!=value):
    if(userInput == "scissor"):
        if(value == "rock"):
            print("You Lose")
        else:
            print("You Won")
    elif(userInput == "rock"):
        if(value =="scissor"):
            print("You Won")
        else:
            print("You Lose")
    elif(userInput == "paper"):
        if(value == "scissor"):
            print("You Lose")
        else:
            print("You Won")
    else:
        print("Invalid Input")