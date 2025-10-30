import Python.mastermind.mastermind as mastermind
import colorama
import unittest

RED = colorama.Fore.RED
BLUE = colorama.Fore.BLUE
GREEN = colorama.Fore.GREEN
YELLOW = colorama.Fore.YELLOW
BLACK = colorama.Fore.BLACK
ORANGE = "\x1b[38;5;208m"
RESET = colorama.Style.RESET_ALL

class mastermindTest(unittest.TestCase):
    def testContainsColour(self):
        self.assertFalse(mastermind.containsColour("rgb", "w"))
        self.assertTrue(mastermind.containsColour("rgb","g"))

    def testconcatClues(self):
        self.assertEqual(mastermind.concatClues(2, 3), f"{RED}Correct {RESET}{RED}Correct {RESET}Close Close Close ") 
        self.assertEqual(mastermind.concatClues(0, 3), f"Close Close Close ") 
        self.assertEqual(mastermind.concatClues(2, 0), f"{RED}Correct {RESET}{RED}Correct {RESET}") 
        self.assertEqual(mastermind.concatClues(0, 0), "") 

    def testIsColour(self):
        self.assertTrue(mastermind.isColour("rgbw"))
        self.assertFalse(mastermind.isColour("rtgb"))
        self.assertFalse(mastermind.isColour("@rgb"))
    
    def testGenCombo(self):
        self.assertTrue(len(mastermind.genCombo())==4)

if __name__ == '__main__':
    unittest.main()