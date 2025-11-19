import mastermind
import colorama
import unittest

#if for some reason you terminal does not support escape code colouring, use the colorama version of the colour variables. orange will not work

RED = "\x1b[38;2;232;45;45m" 
#RED = colorama.Fore.RED
CORRECTRED = "\x1b[38;2;255;0;0m"
ORANGE = "\x1b[38;2;255;127;0m"
YELLOW = "\x1b[38;2;223;223;40m" 
#YELLOW = colorama.Fore.YELLOW
GREEN = "\x1b[38;2;71;211;71m" 
#GREEN = colorama.Fore.GREEN
BLUE = "\x1b[38;2;0;149;255m" 
#BLUE = colorama.Fore.BLUE
WHITE = "\x1b[38;2;255;255;255m" 
#WHITE = colorama.Fore.WHITE
BLACK = "\x1b[38;2;0;0;0m" 
#BLACK = colorama.Fore.BLACK
RESET = "\x1b[0m" 
#RESET = colorama.Style.RESET_ALL

def genComboChecker(combo: str, comboDict: dict):
    for i, col in enumerate(combo):
        if i not in comboDict[col][1]:
            return False
    return True

class mastermindTest(unittest.TestCase):
    def testConcatClues(self):
        self.assertEqual(mastermind.concatClues(2, 3), f"{CORRECTRED}Correct Correct {WHITE}Close Close Close {RESET}") 
        self.assertEqual(mastermind.concatClues(0, 3), f"{CORRECTRED}{WHITE}Close Close Close {RESET}") 
        self.assertEqual(mastermind.concatClues(2, 0), f"{CORRECTRED}Correct Correct {WHITE}{RESET}") 
        self.assertEqual(mastermind.concatClues(0, 0), f"{CORRECTRED}{WHITE}{RESET}") 

    def testGetClues(self):
        self.assertEqual(mastermind.getClues("rgbw", "yoyo", {"r": [1, [0]], "o": [0, []], "y": [0, []], "g": [1, [1]], "b": [1, [2]], "w": [1, [3]], "-": [0, []]}), f"{BLACK}None{RESET}") 
        self.assertEqual(mastermind.getClues("rgbw", "rgbw", {"r": [1, [0]], "o": [0, []], "y": [0, []], "g": [1, [1]], "b": [1, [2]], "w": [1, [3]], "-": [0, []]}), "Congratulations! Your guess is correct!")
        self.assertEqual(mastermind.getClues("rgbw", "rgwb", {"r": [1, [0]], "o": [0, []], "y": [0, []], "g": [1, [1]], "b": [1, [2]], "w": [1, [3]], "-": [0, []]}), f"{CORRECTRED}Correct Correct {WHITE}Close Close {RESET}")
        self.assertEqual(mastermind.getClues("rrbw", "rrrr", {"r": [2, [0, 1]], "o": [0, []], "y": [0, []], "g": [0, []], "b": [1, [2]], "w": [1, [3]], "-": [0, []]}), f"{CORRECTRED}Correct Correct {WHITE}{RESET}")  
        self.assertEqual(mastermind.getClues("bwrr", "rrrr", {"r": [2, [2, 3]], "o": [0, []], "y": [0, []], "g": [0, []], "b": [1, [0]], "w": [1, [1]], "-": [0, []]}), f"{CORRECTRED}Correct Correct {WHITE}{RESET}")  
        self.assertEqual(mastermind.getClues("rbwr", "rrrr", {"r": [2, [0, 3]], "o": [0, []], "y": [0, []], "g": [0, []], "b": [1, [1]], "w": [1, [2]], "-": [0, []]}), f"{CORRECTRED}Correct Correct {WHITE}{RESET}")  
        self.assertEqual(mastermind.getClues("brwr", "rrrr", {"r": [2, [1, 3]], "o": [0, []], "y": [0, []], "g": [0, []], "b": [1, [0]], "w": [1, [2]], "-": [0, []]}), f"{CORRECTRED}Correct Correct {WHITE}{RESET}")  
        self.assertEqual(mastermind.getClues("brwr", "rooo", {"r": [2, [1, 3]], "o": [0, []], "y": [0, []], "g": [0, []], "b": [1, [0]], "w": [1, [2]], "-": [0, []]}), f"{CORRECTRED}{WHITE}Close {RESET}")  
        self.assertEqual(mastermind.getClues("brwr", "oroo", {"r": [2, [1, 3]], "o": [0, []], "y": [0, []], "g": [0, []], "b": [1, [0]], "w": [1, [2]], "-": [0, []]}), f"{CORRECTRED}Correct {WHITE}{RESET}")    
        self.assertEqual(mastermind.getClues("oygg", "rgrg", {"r": [0, []], "o": [1, [0]], "y": [1, [1]], "g": [2, [2, 3]], "b": [0, [0]], "w": [0, []], "-": [0, []]}), f"{CORRECTRED}Correct {WHITE}Close {RESET}")
    
    def testIsColour(self):
        self.assertTrue(mastermind.isColour("rgbw"))
        self.assertFalse(mastermind.isColour("rtgb"))
        self.assertFalse(mastermind.isColour("@rgb"))
        self.assertTrue(mastermind.isColour(""))
    
    def testGenComboChecker(self):
        self.assertTrue(genComboChecker("rgbw", {"r": [1, [0]], "o": [0, []], "y": [0, []], "g": [1, [1]], "b": [1, [2]], "w": [1, [3]], "-": [0, []]}))
        self. assertFalse(genComboChecker("rgbw", {"r": [2, [0, 1]], "o": [0, []], "y": [0, []], "g": [0, []], "b": [1, [2]], "w": [1, [3]], "-": [0, []]}))

    def testGenCombo(self):
        combo,comboDict = mastermind.genCombo()
        self.assertTrue(len(combo)==4 and genComboChecker(combo, comboDict))

    def testColourOutput(self):
        self.assertEqual(mastermind.colourOutput("royg"), f"{RED}r{ORANGE}o{YELLOW}y{GREEN}g{RESET}")

if __name__ == '__main__':
    unittest.main()