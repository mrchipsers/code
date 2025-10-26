#import random
import colorama
#import pygame
#import os

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

def pMakeColour(combo):
    colouredWord=""
    if combo[0]=="r":
        colouredWord+=f"{RED}{combo}{RESET}"
    elif combo[0]=="b":
        colouredWord+=f"{BLUE}{combo}{RESET}"
    elif combo[0]=="g":
        colouredWord+=f"{GREEN}{combo}{RESET}"
    elif combo[0]=="y":
        colouredWord+=f"{YELLOW}{combo}{RESET}"
    elif combo[0]=="o":
        colouredWord+=f"{ORANGE}{combo}{RESET}"
    else:
        colouredWord+=combo
    return colouredWord

textStr = ["you will have 10 guesses to guess a 4 colour combination consisting of the colours ", "red", ", ", "blue", ", ", "green", ", ", "yellow", ", ", "orange", ", ", "and white."]
output=""
for i in range(len(textStr)):
    if i == 0:
        output += "".join(textStr[i])
        continue
    else:
        output += "".join(pMakeColour(textStr[i]))
print(output)
