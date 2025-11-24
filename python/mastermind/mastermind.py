import random
from prompt_toolkit import ANSI
from prompt_toolkit.lexers import Lexer
from prompt_toolkit.shortcuts import prompt

RED = "\x1b[38;2;232;45;45m" 
CORRECTRED = "\x1b[38;2;255;0;0m"
ORANGE = "\x1b[38;2;255;127;0m"
YELLOW = "\x1b[38;2;223;223;40m" 
GREEN = "\x1b[38;2;71;211;71m" 
BLUE = "\x1b[38;2;0;149;255m" 
WHITE = "\x1b[38;2;255;255;255m" 
BLACK = "\x1b[38;2;0;0;0m" 
RESET = "\x1b[0m" 

#leaderboardPath='leaderboard.txt' #this is for normal computers
leaderboardPath='python/mastermind/leaderboard.txt' #my computer is messed up

with open(leaderboardPath, 'r') as f:
    leaderboard = []
    for i, line in enumerate(f.readlines()):
        line.replace('\n','')
        line = line.split()
        leaderboard.append(line)

def sortLeader(new: list):
    for i, pos in enumerate(leaderboard):
        if pos[0] > new[0]:
            leaderboard.insert(i, [f"{int(new[0])+1}", new[1]])
            return
    leaderboard.append(new)
    
    with open(leaderboardPath, 'w') as f:    
        for entry in leaderboard:
            f.write(f"{entry[0]} {entry[1]}\n")

def printLeader(max: int):
    print("posistion   guesses    name")
    for i, pos in enumerate(leaderboard):
        if i==max:
            break
        print(f"{i+1}{" "*(12-len(f"{i+1}"))}{pos[0]}{" "*(11-len(pos[0]))}{pos[1]}")

class mastermindLexer(Lexer):

    def lex_document(self, document):
        mastermindCol = {
            "r": "#e82d2d",  
            "o": "#ff7f00",  
            "y": "#dfdf28",  
            "g": "#47d347",  
            "b": "#0095ff",  
            "w": "#ffffff"
        }

        def getLetter(lineno):
            input = []
            for c in document.lines[lineno]:
                colour = mastermindCol.get(c.lower())
                if colour:
                    style_spec = f"fg:{colour}"
                else:
                    style_spec = ""
                input.append((style_spec, c))
            return input
        return getLetter

def instructions():
    print(f"""you will have 10 guesses to guess a 4 colour combination consisting of the colours {RED}red{RESET}, {ORANGE}orange{RESET}, {YELLOW}yellow{RESET}, {GREEN}green{RESET}, {BLUE}blue{RESET}, and {WHITE}white{RESET}. 
To input the letters, input the first letters of each colour, repeats are allowed. 
Ex. for the input red, yellow, blue, green, you will input {RED}r{YELLOW}y{BLUE}b{GREEN}g{RESET}. 
After each incorrect guess, you will be given clues categorized as follows:""")
    print("Clue:\t\tMeaning:")
    print(f"{BLACK}None{RESET}\t\tNone of the digits in your guess is correct.")
    print(f"{WHITE}Close{RESET}\t\tOne colour is correct but in the wrong position.")
    print(f"{CORRECTRED}Correct{RESET}\t\tOne colour is correct and in the correct position.")

def genCombo():
    options = ["r", "o", "y", "g", "b", "w"]
    combo = []
   
    for i in range(4):    
        random.shuffle(options)
        combo.append(options[0])

    scombo = "".join(combo)
    return scombo

def concatClues(countAt: int, countClose: int):
    return (f"{CORRECTRED}{"Correct "*countAt}")+(f"{WHITE}{"Close "*countClose}{RESET}")

def getClues(secretCombo: str, userGuess: str):
    close = 0
    on = 0
    listGuess = list(userGuess)
    listAns = list(secretCombo)

    if secretCombo==userGuess:
        return "Congratulations! Your guess is correct!"
    
    for i, col in enumerate(listGuess):
        if col==listAns[i]:
            listAns[i]="-"
            listGuess[i]="_"
            on+=1
    
    for i, col in enumerate(listGuess):
        if col in listAns:
            listGuess[i]="_"
            close+=1

    if on==0 and close==0:
        return f"{BLACK}None{RESET}"
   
    return concatClues(on, close)

def colourOutput(combo: str):
    colouredWord=""
    for i in combo:
        if i=="r":
            colouredWord+=f"{RED}r"
        elif i=="o":
            colouredWord+=f"{ORANGE}o"
        elif i=="y":
            colouredWord+=f"{YELLOW}y"
        elif i=="g":
            colouredWord+=f"{GREEN}g"
        elif i=="b":
            colouredWord+=f"{BLUE}b"
        else:
            colouredWord+=f"{WHITE}w"
    return colouredWord+f"{RESET}"    

def isColour(userGuess: str):
    for i in userGuess:
        if i not in "roygbw":
            return False
    return True

def validIn(userGuess):
    while True:
        if len(userGuess)==4 and isColour(userGuess):
            return userGuess
            
        userGuess = prompt(ANSI(f"guess a combination that is 4 letters long and contains the letters {RED}r{ORANGE}o{YELLOW}y{GREEN}g{BLUE}b{WHITE}w{RESET}: "), lexer=mastermindLexer()).lower()

def playRound(secretCombo: str):
    for i in range(10):
        guess = prompt(ANSI(f"guess number {i+1}:"), lexer=mastermindLexer()).lower()
        guess = validIn(guess)

        if getClues(secretCombo, guess)=="Congratulations! Your guess is correct!":
            print("Congratulations! Your guess is correct!")
            return i
        else:
            print(getClues(secretCombo, guess))
    
    print(f"You ran out of guesses. The answer was {colourOutput(secretCombo)}. GAME OVER!!! Thanks for playing!")
    return "DNF"

def runGame():
    run = True
    while(run): 
        secretCombo = genCombo()
        instructions()
        name = mastermindDebug(secretCombo)
        guesses = str(playRound(secretCombo))
        sortLeader([guesses, name])
        print("this is the top ten leaderboard: ")
        printLeader(10)
        if input("would you like the full leaderboard? (y/N)").lower()=="y":
            printLeader(1000000)
        if input("would you like to play again? (y/N)").lower()!="y":
            run = False 
    
def mastermindDebug(secretCombo):
    name = input("enter your name: ")
    if name.lower() in ["admin"]:
        print(colourOutput(secretCombo))
        print(f"Hi {name}, get ready to play!")
        return name
    print(f"Hi {name}, get ready to play!")
    return name

if __name__ == '__main__':
    runGame()
    