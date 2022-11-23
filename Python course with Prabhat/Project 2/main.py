import random
randNumber = random.randint(1,100)
print(randNumber)
userGuess = None
Guesses = 0

while(userGuess!= randNumber):
    userGuess = int(input("Enter the number: "))
    Guesses += 1
    if (userGuess==randNumber):
        print("You guessed it correct")
    else:
        if(userGuess>randNumber):
            print("you guessed it wrong! Enter the smaller number")
        else:
            print("You guessed it wrong! Enter the larger number")
print(f"You guessed the number {Guesses} guesses")

with open("Project 2/hiscore.txt","r") as f:
    hiscore = int(f.read())

if (hiscore>Guesses):
    print("You have broken the hiscore")
    with open("Project 2/hiscore.txt","w") as f:
        f.write(str(Guesses))
