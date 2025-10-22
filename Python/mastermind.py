import random
import colorama
ORANGE = "\x1b[38;5;208m"
def instructions(maxGuesses: int):
    print(f"""you will have {maxGuesses} guesses to guess a 4 colour combination consisting of the colours {colorama.Fore.RED}red{colorama.Style.RESET_ALL}, {colorama.Fore.BLUE}blue{colorama.Style.RESET_ALL}, {colorama.Fore.GREEN}green{colorama.Style.RESET_ALL}, {colorama.Fore.YELLOW}yellow{colorama.Style.RESET_ALL}, {ORANGE}orange{colorama.Style.RESET_ALL}, and white. 
    to input the letters, input the first letters of each colour, with no repeats. 
    Ex. for the input red, yellow, blue, green, you will input rybg. 
    After each incorrect guess, you will be given clues categorized as follows:""")
    print("Clue:\t\tMeaning:")
    print(f"{colorama.Fore.BLACK}None{colorama.Style.RESET_ALL}\t\tNone of the digits in your guess is correct.")
    print(f"Close\t\tOne digit is correct but in the wrong position.")
    print(f"{colorama.Fore.RED}@{colorama.Style.RESET_ALL}\t\tOne digit is correct and in the right position.")

def containsCharacter(word: str, literal: str):
    return literal in word

def generatesecretCombo():
    options = [f"{colorama.Fore.RED}r{colorama.Style.RESET_ALL}", f"{colorama.Fore.BLUE}b{colorama.Style.RESET_ALL}", f"{colorama.Fore.GREEN}g{colorama.Style.RESET_ALL}", f"{colorama.Fore.YELLOW}y{colorama.Style.RESET_ALL}", f"{ORANGE}o{colorama.Style.RESET_ALL}", f"w"]
    random.shuffle(options)
    options = options[:4]
    return "".join(options)

def concatenateClues(countAt: int, countClose: int):
    clue = ""
    for i in range(countAt):
        clue+=f"{colorama.Fore.GREEN}@ {colorama.Style.RESET_ALL}"
    for i in range(countClose):
        clue+=f"{colorama.Fore.RED}Close {colorama.Style.RESET_ALL}"
    return clue

def getClues(secretCombo: str, userGuess: str):
    close = 0
    on = 0

    if secretCombo==userGuess:
        return "Congratulations! Your guess is correct!"
    
    for i, name in enumerate(userGuess):
        if secretCombo[i]==name:
            on+=1
        elif containsCharacter(secretCombo, name):
            close+=1
    
    if on==0 and close==0:
        return f"{colorama.Fore.BLACK}None{colorama.Style.RESET_ALL}"
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
        if i not in "rbgyow":
            return False

    return True

def valid(userGuess: str):
    while True:
        if isLetter(userGuess) and len(userGuess)==4:
            return userGuess
        
        userGuess = input("guess a number that is 4 letters long and contains the letters rbgyow: ")

#runGame()
instructions(10)
print(generatesecretCombo())