import random
import colorama
from prompt_toolkit import ANSI
from prompt_toolkit.lexers import Lexer
from prompt_toolkit.shortcuts import prompt


RED = colorama.Fore.RED
BLUE = colorama.Fore.BLUE
GREEN = colorama.Fore.GREEN
YELLOW = colorama.Fore.YELLOW
BLACK = colorama.Fore.BLACK
ORANGE = "\x1b[38;5;208m"
RESET = colorama.Style.RESET_ALL

class mastermindLexer(Lexer):

    def lex_document(self, document):
        mastermindCol = {
            "r": "#e82d2d",  
            "o": "#ff7f00",  
            "y": "#cccc04",  
            "g": "#47d347",  
            "b": "#0095ff",  
        }

        def getLetter(lineno):
            fragments = []
            for c in document.lines[lineno]:
                colour = mastermindCol.get(c.lower())
                if colour:
                    style_spec = f"fg:{colour}"
                else:
                    style_spec = ""
                fragments.append((style_spec, c))
            return fragments
        return getLetter


def instructions():
    print(f"""you will have 10 guesses to guess a 4 colour combination consisting of the colours {RED}red{RESET}, {BLUE}blue{RESET}, {GREEN}green{RESET}, {YELLOW}yellow{RESET}, {ORANGE}orange{RESET}, and white. To input the letters, input the first letters of each colour, with no repeats. Ex. for the input red, yellow, blue, green, you will input {RED}r{YELLOW}y{BLUE}b{GREEN}g{RESET}. After each incorrect guess, you will be given clues categorized as follows:""")
    print("Clue:\t\tMeaning:")
    print(f"{BLACK}None{RESET}\t\tNone of the digits in your guess is correct.")
    print(f"Close\t\tOne digit is correct but in the wrong position.")
    print(f"{RED}@{RESET}\t\tOne digit is correct and in the right position.")

def containsCharacter(word: str, literal: str):
    return literal in word

def generatesecretCombo():
    options = ["r", "b", "g", "y", "o", "w"]
    combo = []
    for i in range(4):    
        random.shuffle(options)
        combo.append(options[0])
    combo = "".join(combo)
    return combo

def moreThanOne(word: str, literal: str):
    count=0
    for i in word:
        if i==literal:
            count+=1
    return count>1

def concatenateClues(countAt: int, countClose: int):
    clue = ""
    for i in range(countAt):
        clue+=f"{RED}@ {RESET}"
    for i in range(countClose):
        clue+=f"Close "
    return clue

def getClues(secretCombo: str, userGuess: str):
    close = 0
    on = 0
    seen = []
    if secretCombo==userGuess:
        return "Congratulations! Your guess is correct!"
    
    for i, col in enumerate(userGuess):
        if col in seen:
            continue
        if secretCombo[i]==col:
            on+=1
            seen.append(col)
        elif containsCharacter(secretCombo, col):
            close+=1
            seen.append(col)
    
    if on==0 and close==0:
        return f"{BLACK}None{RESET}"
    return concatenateClues(on, close)
    
def playRound(secretCombo: str):
    for i in range(10):
        guess = prompt(f"guess number {i+1}: ", lexer=mastermindLexer())
        guess = valid(guess)

        if getClues(secretCombo, guess)=="Congratulations! Your guess is correct!":
            print("Congratulations! Your guess is correct!")
            return
        else:
            print(getClues(secretCombo, guess))
    
    print(f"You ran out of guesses. The answer was {makeColour(secretCombo)}. GAME OVER!!! Thanks for playing!")

def makeColour(combo):
    colouredWord=""
    for i in combo:
        if i=="r":
            colouredWord+=f"{RED}r{RESET}"
        elif i=="b":
            colouredWord+=f"{BLUE}b{RESET}"
        elif i=="g":
            colouredWord+=f"{GREEN}g{RESET}"
        elif i=="y":
            colouredWord+=f"{YELLOW}y{RESET}"
        elif i=="o":
            colouredWord+=f"{ORANGE}o{RESET}"
        else:
            colouredWord+="w"
    return colouredWord

def runGame():
    secretCombo = generatesecretCombo()
    instructions()
    print(secretCombo)
    playRound(secretCombo)

def isLetter(userGuess: str):
    for i in userGuess:
        if i not in "rbgyow":
            return False

    return True

def valid(userGuess: str):
    while True:
        if isLetter(userGuess) and len(userGuess)==4:
            return userGuess
            
        userGuess = prompt(ANSI(f"guess a number that is 4 letters long and contains the letters {RED}r{BLUE}b{GREEN}g{YELLOW}y{ORANGE}o{RESET}w: "), lexer=mastermindLexer())

runGame()
