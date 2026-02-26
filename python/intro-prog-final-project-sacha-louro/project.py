"""
Intro to Programming – Final Project
Student Name: Sacha Louro
Project Title: Mastermind

Description:
play rounds of the game mastermind on the command line.

Instructions:
run the game however you like to run python programs (python3 project.py, press the play button in vs code). asks for user name, takes user guess and returns clues, outputs leaderboard when done, asks if play again
"""

import random
from prompt_toolkit import ANSI
from prompt_toolkit.lexers import Lexer
from prompt_toolkit.shortcuts import prompt
import getpass

RED = "\x1b[38;2;232;45;45m" 
CORRECTRED = "\x1b[38;2;255;0;0m"
ORANGE = "\x1b[38;2;255;127;0m"
YELLOW = "\x1b[38;2;223;223;40m" 
GREEN = "\x1b[38;2;71;211;71m" 
BLUE = "\x1b[38;2;0;149;255m" 
WHITE = "\x1b[38;2;255;255;255m" 
BLACK = "\x1b[38;2;127;127;127m" 
PURPLE = "\x1b[38;2;198;0;209m"
RESET = "\x1b[0m" 

leaderboardPath="python/intro-prog-final-project-sacha-louro/leaderboard.txt" 

#opens the leaderboard file and writes the lines as elements in a list, returs said list
def openLeader():
    with open(leaderboardPath, 'r') as f:
        leaderboard = []
        for line in f.readlines():
            line = line.split()
            leaderboard.append(line)
    return leaderboard

#sorts new entries into the leaderboard list based on number of guesses, lower is better. returns index of sorted element
def sortLeader(name: str, num: str, leaderboard: list):
    for i, pos in enumerate(leaderboard):
        if pos[0] > num:
            leaderboard.insert(i, [f"{int(num)+1}", name])
            return i
    leaderboard.append([num, name])
    return len(leaderboard)-1
    
#writes the leaderboard back into the leaderboard text file
def saveLeader(leaderboard: list):  
    with open(leaderboardPath, 'w') as f:    
        for entry in leaderboard:
            f.write(f"{entry[0]} {entry[1]}\n")

#prints the leaderboard to the command line, highlights the current user's position
def printLeader(max: int, leaderboard: list, you: int):
    print("posistion  guesses  name")
    for i in range(min(max, len(leaderboard))):
        if i==you:
            print(f"{PURPLE}{i+1:<11}{leaderboard[i][0]:9}{leaderboard[i][1]}{RESET}")
        else:    
            print(f"{i+1:<11}{leaderboard[i][0]:9}{leaderboard[i][1]}")

#lexer to colour user input as it is happening
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

#prints instructions to command line
def instructions():
    print(f"""you will have 10 guesses to guess a 4 colour combination consisting of the colours {RED}red{RESET}, {ORANGE}orange{RESET}, {YELLOW}yellow{RESET}, {GREEN}green{RESET}, {BLUE}blue{RESET}, and {WHITE}white{RESET}. 
To input the letters, input the first letters of each colour, repeats are allowed. 
Ex. for the input red, yellow, blue, green, you will input {RED}r{YELLOW}y{BLUE}b{GREEN}g{RESET}. 
After each incorrect guess, you will be given clues categorized as follows:""")
    print("Clue:\t\tMeaning:")
    print(f"{BLACK}None{RESET}\t\tNone of the digits in your guess is correct.")
    print(f"{WHITE}Close{RESET}\t\tOne colour is correct but in the wrong position.")
    print(f"{CORRECTRED}Correct{RESET}\t\tOne colour is correct and in the correct position.")

#generates a random len 4 string from the options, returns it
def genCombo(multiplayer: bool, round: int):
    if multiplayer:
        return getpass.getpass(prompt=f"player {round%2}, enter your combo: ")
    else:
        options = ["r", "o", "y", "g", "b", "w"]
        return "".join(random.choices(options, k=4))
    

#makes the clues to be printed from the user's guess. takes number of close and exact entries, returns string with those numbers
def concatClues(countAt: int, countClose: int):
    return (f"{CORRECTRED}{"Correct "*countAt}")+(f"{WHITE}{"Close "*countClose}{RESET}")

#gets the number of close and correct entries from the user guess compared to correct answer.
#takes user input and correct combo and outputs win, none, or the result of concatClues based on how the user did 
def getClues(secretCombo: str, userGuess: str):
    close = 0
    on = 0
    listGuess = list(userGuess)
    listAns = list(secretCombo)

    if secretCombo==userGuess:
        return "win"
    for i, col in enumerate(listGuess):
        if col==listAns[i]:
            listAns[i]="-"
            listGuess[i]="_"
            on+=1
    for i, col in enumerate(listGuess):
        if col in listAns:
            listAns[listAns.index(col)]="-"
            listGuess[i]="_"
            close+=1
    if on==0 and close==0:
        return f"{BLACK}None{RESET}"
    return concatClues(on, close)

#takes the uncoloured input and colourises it based on the letters. returns colourised string
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
    return colouredWord+RESET   

#makes sure that every element of the user's guess is a valid element (an option for the combo). returns bool depending on validity
def isColour(userGuess: str):
    return set(userGuess)<=set("roygbw")

#makes sure user's guess is correct len and contains only valid elements. reprompts for correct input until input is valid. returns valid input
def validIn(userGuess: str):
    while not (len(userGuess) == 4 and isColour(userGuess)):
        userGuess = prompt(ANSI(f"guess a combination that is 4 letters long and contains the letters {RED}r{ORANGE}o{YELLOW}y{GREEN}g{BLUE}b{WHITE}w{RESET}: "), lexer=mastermindLexer()).lower()
    return userGuess

#main function to play one round of the game. takes combo, gets user input, gets and prints clues, returns number of guesses required for correct guess on win
def playRound(secretCombo: str):
    for i in range(10):
        guess = validIn(prompt(f"guess number {i+1}: ", lexer=mastermindLexer()).lower())
        clues = getClues(secretCombo, guess)
        
        if clues=="win":
            print(f"{GREEN}Congratulations! Your guess is correct!{RESET}")
            return i
        else:
            print(clues)
    
    print(f"You ran out of guesses. The answer was {colourOutput(secretCombo)}. GAME OVER!")
    return "DNF"

#main function for multiple rounds. gets the leaderboard, combo, plays a round, prints top ten leader, propmts for full leaderboard, prompts to play again. saves leaderboard at end of last round
def runGame(multiplayer: bool):
    leaderboard = openLeader()
    round=1
    play=True
    while(play): 
        secretCombo=genCombo(multiplayer, round)
        instructions()
        if multiplayer:
            print(f"player {(round%2)+1}, get ready to play.")
        you = sortLeader(mastermindDebug(secretCombo), str(playRound(secretCombo)), leaderboard)
        print("this is the top ten leaderboard: ")
        printLeader(10, leaderboard, you)
        saveLeader(leaderboard)
        if input("would you like the full leaderboard? (y/N)").lower()=="y":
            printLeader(1000000, leaderboard, you)
        if input("would you like to play again? (y/N)").lower()!="y":
            play=False 
        round+=1
    print("Thanks for playing!")

# prompts user for name. if the name is one of the admin names, prints combo to facilitate debugging. greets player and returns name for the leaderboard.
def mastermindDebug(secretCombo: str):
    name = input("enter your name: ")
    if name.lower() in ["admin", "test"]:
        print(colourOutput(secretCombo))
    print(f"Hi {name}, get ready to play!")
    return name

def multiplayer():
    nUsers=input("Would you like to play a single or multiplayer game (S/m): ")
    if nUsers.lower()=="s":
        runGame(False)
    else:
        runGame(True)

if __name__ == '__main__':
    multiplayer()  