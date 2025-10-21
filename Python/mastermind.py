import random
def instructions(maxGuesses: int):
    print(f"you will have {maxGuesses} guesses to guess a 4 letter combination consisting of the letters r, o ,y, g, b, p, and s. After each incorrect guess, you will be given clues categorized as follows:")
    print("Clue:\t\tMeaning:")
    print("None\t\tNone of the digits in your guess is correct.")
    print("Close\t\tOne digit is correct but in the wrong position.")
    print("@\t\tOne digit is correct and in the right position.")

def containsCharacter(word: str, literal: str):
    return literal in word

def generatesecretCombo():
    options = ["r", "o", "y", "g", "b", "p", "s"]
    random.shuffle(options)
    options = options[:4]
    return "".join(options)

def concatenateClues(countAt: int, countClose: int):
    clue = ""
    for i in range(countAt):
        clue+="@ "
    for i in range(countClose):
        clue+="Close "
    return clue

def getClues(secretCombo: str, userGuess: str):
    close = 0
    on = 0

    if secretCombo==userGuess:
        return "Congratulations! Your guess is correct!"
    
    for i in range(len(userGuess)):
        if containsCharacter(secretCombo, userGuess[i])!=True:
            continue
        elif secretCombo[i]==userGuess[i]:
            on+=1
        else:
            close+=1
    
    if on==0 and close==0:
        return "None"
    else:
        return concatenateClues(on, close)
    
def playRound(secretCombo: str, maxGuesses: int):
    for i in range(maxGuesses):
        guess = input(f"guess number {i+1}: ")
        guess = valid(guess)

        if getClues(secretCombo, guess)=="Congratulations! Your guess is correct!":
            print("Congratulations! Your guess is correct!")
            return
        else:
            print(getClues(secretCombo, guess))
    print(f"You ran out of guesses. The answer was {secretCombo}. GAME OVER!!! Thanks for playing!")

def runGame():
    maxGuesses = int(input("Enter the number of guesses the player has: "))
    secretCombo = generatesecretCombo()
    instructions(maxGuesses)
    print(secretCombo)
    playRound(secretCombo, maxGuesses)

def isLetter(userGuess: str):
    for i in userGuess:
        if i not in "roygbps":
            return False

    return True

def valid(userGuess: str):
    while True:
        if isLetter(userGuess) and len(userGuess)==4:
            return userGuess
        
        userGuess = input(f"guess a number that is 4 letters long and contains the letters r, o ,y, g, b, p, and s: ")
    
runGame()