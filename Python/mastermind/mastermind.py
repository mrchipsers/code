import random
import colorama
from prompt_toolkit import ANSI
from prompt_toolkit.lexers import Lexer
from prompt_toolkit.shortcuts import prompt
import copy

RED = colorama.Fore.RED
BLUE = colorama.Fore.BLUE
GREEN = colorama.Fore.GREEN
YELLOW = colorama.Fore.YELLOW
BLACK = colorama.Fore.BLACK
ORANGE = "\x1b[38;5;208m"
WHITE = colorama.Fore.WHITE
RESET = colorama.Style.RESET_ALL

#leaderboardPath='leaderboard.txt' #this is for normal computers
leaderboardPath='Python/mastermind/leaderboard.txt' #my computer is messed up

with open(leaderboardPath, 'r') as f:
    leaderboard = []
    for i, line in enumerate(f.readlines()):
        line.replace('\n','')
        line = line.split()
        leaderboard.append(line)

class mastermindLexer(Lexer):

    def lex_document(self, document):
        mastermindCol = {
            "r": "#e82d2d",  
            "o": "#ff7f00",  
            "y": "#cccc04",  
            "g": "#47d347",  
            "b": "#0095ff",  
            "w": "#ffffff"
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
    print(f"""you will have 10 guesses to guess a 4 colour combination consisting of the colours {RED}red{RESET}, {ORANGE}orange{RESET}, {YELLOW}yellow{RESET}, {GREEN}green{RESET}, {BLUE}blue{RESET}, and white. 
To input the letters, input the first letters of each colour, repeats are allowed. 
Ex. for the input red, yellow, blue, green, you will input {RED}r{YELLOW}y{BLUE}b{GREEN}g{RESET}. 
After each incorrect guess, you will be given clues categorized as follows:""")
    print("Clue:\t\tMeaning:")
    print(f"{BLACK}None{RESET}\t\tNone of the digits in your guess is correct.")
    print(f"Close\t\tOne colour is correct but in the wrong position.")
    print(f"{RED}Correct{RESET}\t\tOne colour is correct and in the correct position.")

def containsColour(combo: str, colour: str):
    return colour in combo

def genCombo():
    comboDict = {
    "r": [0, []],
    "o": [0, []],
    "y": [0, []],
    "g": [0, []],
    "b": [0, []],
    "w": [0, []],
    "-": [0, []]
    }
    options = ["r", "o", "y", "g", "b", "w"]
    combo = []
   
    for i in range(4):    
        random.shuffle(options)
        combo.append(options[0])
        comboDict[options[0]][0]+=1
        comboDict[options[0]][1].append(i)
    scombo = "".join(combo)

    return [scombo,comboDict]

def concatClues(countAt: int, countClose: int):
    return (f"{RED}Correct {RESET}"*countAt)+("Close "*countClose)

def getClues(secretCombo: str, userGuess: str, comboDict: dict):
    comboDictCopy=copy.deepcopy(comboDict)
    close = 0
    on = 0
    listGuess = list(userGuess)

    if secretCombo==userGuess:
        return "Congratulations! Your guess is correct!"
    
    for i, colour in enumerate(listGuess):
        if comboDictCopy[colour][0]>0 and i in comboDictCopy[colour][1]:
            on+=1
            comboDictCopy[colour][0]-=1
            listGuess[i]="-"
    
    for i, colour in enumerate(listGuess):
        if comboDictCopy[colour][0]>0:
            close+=1
            comboDictCopy[colour][0]-=1
    
    if on==0 and close==0:
        return f"{BLACK}None{RESET}"
   
    return concatClues(on, close)

def colourOutput(combo: str):
    colouredWord=""
    for i in combo:
        if i=="r":
            colouredWord+=f"{RED}r{RESET}"
        elif i=="o":
            colouredWord+=f"{ORANGE}o{RESET}"
        elif i=="y":
            colouredWord+=f"{YELLOW}y{RESET}"
        elif i=="g":
            colouredWord+=f"{GREEN}g{RESET}"
        elif i=="b":
            colouredWord+=f"{BLUE}b{RESET}"
        else:
            colouredWord+=f"{WHITE}w{RESET}"
    return colouredWord    

def isColour(userGuess: str):
    for i in userGuess:
        if i not in "roygbw":
            return False

    return True

def validIn(userGuess: str):
    while True:
        if isColour(userGuess) and len(userGuess)==4:
            return userGuess
            
        userGuess = prompt(ANSI(f"guess a number that is 4 letters long and contains the letters {RED}r{ORANGE}o{YELLOW}y{GREEN}g{BLUE}b{RESET}w: "), lexer=mastermindLexer()).lower()

def sortLeader(entry):
    for i, pos in enumerate(leaderboard):
        if pos[0] > entry[0]:
            leaderboard.insert(i, entry)
            return
    leaderboard.append(entry)

def saveLeader():
    with open(leaderboardPath, 'w') as f:
        for entry in leaderboard:
            guesses = entry[0]
            name = entry[1]
            f.write(f"{guesses} {name}\n")

def printLeader():
    print("posistion  guesses  name")
    for i, pos in enumerate(leaderboard):
        guesses = pos[0]
        name = pos[1]
        if i==9 and guesses=="DNF":
            print(f"{i+1}         {guesses}      {name}")
            break
        elif i==9:
            print(f"{i+1}         {guesses}        {name}")
            break
        elif guesses=="DNF":
            print(f"{i+1}          {guesses}      {name}")
        else:
            print(f"{i+1}          {guesses}        {name}")

def playRound(secretCombo: str, comboDict: dict):
    for i in range(10):
        guess = prompt(f"guess number {i+1}: ", lexer=mastermindLexer()).lower()
        guess = validIn(guess)

        if getClues(secretCombo, guess, comboDict)=="Congratulations! Your guess is correct!":
            print("Congratulations! Your guess is correct!")
            return i+1
        else:
            print(getClues(secretCombo, guess, comboDict))
    
    print(f"You ran out of guesses. The answer was {colourOutput(secretCombo)}. GAME OVER!!! Thanks for playing!")
    return "DNF"

def runGame():
    combo = genCombo()
    secretCombo, comboDict = combo[0], combo[1]
    instructions()
    name = str(mastermindDebug(secretCombo))
    guesses = str(playRound(secretCombo, comboDict))
    sortLeader([guesses, name])
    saveLeader()
    print("this is the top ten leaderboard: ")
    printLeader()
    

def mastermindDebug(secretCombo):
    name = input("enter your name: ")
    if name.lower()=="admin" or name.lower()=="sofia":
        print(colourOutput(secretCombo))
        return name
    else: 
        print(f"Hi {name}, get ready to play!")
        return name

if __name__ == '__main__':
    runGame()