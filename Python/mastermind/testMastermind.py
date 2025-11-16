import mastermind
import colorama
import unittest

RED = "\x1b[38;2;232;45;45m" #colorama.Fore.RED
CORRECTRED = "\x1b[38;2;255;0;0m"
ORANGE = "\x1b[38;2;255;127;0m"
YELLOW = "\x1b[38;2;223;223;40m" #colorama.Fore.YELLOW
GREEN = "\x1b[38;2;71;211;71m" #colorama.Fore.GREEN
BLUE = "\x1b[38;2;0;149;255m" #colorama.Fore.BLUE
WHITE = "\x1b[38;2;255;255;255m" #colorama.Fore.WHITE
BLACK = "\x1b[38;2;0;0;0m" #colorama.Fore.BLACK
RESET = "\x1b[0m" #colorama.Style.RESET_ALL

class mastermindTest(unittest.TestCase):
    def testContainsColour(self):
        self.assertFalse(mastermind.containsColour("rgb", "w"))
        self.assertTrue(mastermind.containsColour("rgb","g"))

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
    def testIsColour(self):
        self.assertTrue(mastermind.isColour("rgbw"))
        self.assertFalse(mastermind.isColour("rtgb"))
        self.assertFalse(mastermind.isColour("@rgb"))
    
    def testGenCombo(self):
        self.assertTrue(len(mastermind.genCombo()[0])==4)

if __name__ == '__main__':
    unittest.main()