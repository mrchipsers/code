import random
import colorama
import pygame
import os

PWHITE = (0, 0, 0)
RED = colorama.Fore.RED
PRED = (255, 0, 0)
BLUE = colorama.Fore.BLUE
PBLUE = (0, 0, 255)
GREEN = colorama.Fore.GREEN
PGREEN = (0, 255, 0)
YELLOW = colorama.Fore.YELLOW
PYELLOW = (255, 255, 0)
BLACK = colorama.Fore.BLACK
PBLACK = (0, 0 ,0)
ORANGE = "\x1b[38;5;208m"
PORANGE = (38, 5, 208)
RESET = colorama.Style.RESET_ALL


def pyGame():
    pygame.init()
    size = (1000, 1000)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Mastermind")
    clock = pygame.time.Clock()
    
    run = True
    while run:
        clock.tick(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill(PBLACK)
        font = pygame.font.SysFont(pygame.font.get_default_font(), 36)
        textStr1 = ("you will have 10 guesses to guess a 4 colour combination consisting of the colours "  )
        textStr2 = (f"{PRED}red, {PBLUE}blue, {PGREEN}green, {PYELLOW}yellow, {PORANGE}orange, and white.")
        text1 = font.render(textStr1, False, PWHITE)
        text2 = font.render(textStr2, False, PWHITE)
        screen.blit(text1, (0, 0))
        screen.blit(text2, (0,25))

        #pInstructions(screen)
        drawCircles(size, screen)

        pygame.display.flip()

def drawCircles(screenSize: tuple, screen):
    xSpacing = 55
    ySpacing = 70
    cols = 4  
    rows = 10  
    offset_x = (screenSize[0] - (cols - 1) * xSpacing) // 2
    offset_y = (screenSize[1] - (rows - 1) * ySpacing) // 2
    for i in range(cols):
        for j in range(rows):
            x = offset_x + i * xSpacing
            y = offset_y + j * ySpacing +100
            pygame.draw.circle(screen, PBLUE, (x, y), 20)

def pInstructions(screen):
    
    return

def instructions():
    print(f"""you will have 10 guesses to guess a 4 colour combination consisting of the colours {RED}red{RESET}, {BLUE}blue{RESET}, {GREEN}green{RESET}, {YELLOW}yellow{RESET}, {ORANGE}orange{RESET}, and white. 
    to input the letters, input the first letters of each colour, with no repeats. 
    Ex. for the input red, yellow, blue, green, you will input rybg. 
    After each incorrect guess, you will be given clues categorized as follows:""")
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
        guess = input(f"guess number {i+1}: ")
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
        
        userGuess = input(f"guess a number that is 4 letters long and contains the letters {RED}r{BLUE}b{GREEN}g{YELLOW}y{ORANGE}o{RESET}w: ")

def start():
    if input("would you like to use a gui (Y/n): ")=="n":
        runGame()
    else:
        pyGame()

#start()
