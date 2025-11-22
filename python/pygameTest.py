import pygame
import colorama

PWHITE = (255, 255, 255)
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
PORANGE = (255, 165, 0)
RESET = colorama.Style.RESET_ALL

pygame.init()
size=(1000, 1000)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
font = pygame.font.SysFont(pygame.font.get_default_font(), 36)

def pMakeColour(combo):
    colouredWord=""
    if combo[0]=="r":
        text1 = font.render(combo, False, PRED)
        screen.blit(text1, (0, 20))
    elif combo[0]=="b":
        text1 = font.render(combo, False, PBLUE)
        screen.blit(text1, (40, 20))
    elif combo[0]=="g":
        text1 = font.render(combo, False, PGREEN)
        screen.blit(text1, (60, 20))
    elif combo[0]=="y":
        text1 = font.render(combo, False, PYELLOW)
        screen.blit(text1, (90, 20))
    elif combo[0]=="o":
        text1 = font.render(combo, False, PORANGE)
        screen.blit(text1, (120, 20))
    else:
        text1 = font.render(combo, False, PWHITE)
        screen.blit(text1, (150, 20))
    
    

def pyGame():
    # main application loop
    run = True
    while run:
        # limit frames per second
        clock.tick(100)

        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # clear the display (fill black)
        screen.fill(PBLACK)
        
        #font = pygame.font.SysFont(pygame.font.get_default_font(), 36)
        # Remove ANSI color codes (console colorama strings) from text rendered to Pygame.
        #textStr1 = ("you will have 10 guesses to guess a 4 colour combination consisting of the colours "  )
        #textStr2 = (f"{PRED}red, {PBLUE}blue, {PGREEN}green, {PYELLOW}yellow, {PORANGE}orange, and white.")
        #text1 = font.render(textStr1, False, PWHITE)
        #text2 = font.render(textStr2, False, PWHITE)
        #screen.blit(text1, (0, 0))
        #screen.blit(text2, (0,25))

        textStr = ["you will have 10 guesses to guess a 4 colour combination consisting of the colours ", "red", ", ", "blue", ", ", "green", ", ", "yellow", ", ", "orange", ", ", "and white."]
        
        for i in range(len(textStr)):
            if i == 0:
                text1 = font.render(textStr[i], False, PWHITE)
                screen.blit(text1, (0, 0))
                continue
            else:
                pMakeColour(textStr[i])

        
        # draw the scene
        spacing = 55
        cols = 4  # originally x: 50..230 step 60 -> 4 columns
        rows = 10  # originally y: 50..590 step 60 -> 10 rows
        # center the grid on the screen by computing offsets
        offset_x = (size[0] - (cols - 1) * spacing) // 2
        offset_y = (size[1] - (rows - 1) * spacing) // 2
        for i in range(cols):
            for j in range(rows):
                x = offset_x + i * spacing
                y = offset_y + j * spacing
                pygame.draw.circle(screen, (0, 0, 255), (x, y), 20)

        # update the display
        pygame.display.flip()

pyGame()
pygame.quit()
exit()