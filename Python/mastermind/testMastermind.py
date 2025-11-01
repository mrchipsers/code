import mastermind
import colorama
import unittest

RED = colorama.Fore.RED
BLUE = colorama.Fore.BLUE
GREEN = colorama.Fore.GREEN
YELLOW = colorama.Fore.YELLOW
BLACK = colorama.Fore.BLACK
ORANGE = "\x1b[38;5;208m"
RESET = colorama.Style.RESET_ALL

leaderboard = [(2, "sofia"), (3, "Peyton"), (4, "Scarlett")]

def sortLeader(entry):
    for i, pos in enumerate(leaderboard):
        if pos[0] > entry[0]:
            leaderboard.insert(i, entry)
            return leaderboard
    leaderboard.append(entry)

def printLeader():
    for i in leaderboard:
        print(i[0], i[1])

class mastermindTest(unittest.TestCase):
    def testContainsColour(self):
        self.assertFalse(mastermind.containsColour("rgb", "w"))
        self.assertTrue(mastermind.containsColour("rgb","g"))

    def testConcatClues(self):
        self.assertEqual(mastermind.concatClues(2, 3), f"{RED}Correct {RESET}{RED}Correct {RESET}Close Close Close ") 
        self.assertEqual(mastermind.concatClues(0, 3), f"Close Close Close ") 
        self.assertEqual(mastermind.concatClues(2, 0), f"{RED}Correct {RESET}{RED}Correct {RESET}") 
        self.assertEqual(mastermind.concatClues(0, 0), "") 

    def testGetClues(self):
        self.assertEqual(mastermind.getClues("rgbw", "yoyo", {"r": [1, [0]], "o": [0, []], "y": [0, []], "g": [1, [1]], "b": [1, [2]], "w": [1, [3]]}), f"{BLACK}None{RESET}") 
        self.assertEqual(mastermind.getClues("rgbw", "rgbw", {"r": [1, [0]], "o": [0, []], "y": [0, []], "g": [1, [1]], "b": [1, [2]], "w": [1, [3]]}), "Congratulations! Your guess is correct!")
        self.assertEqual(mastermind.getClues("rgbw", "rgwb", {"r": [1, [0]], "o": [0, []], "y": [0, []], "g": [1, [1]], "b": [1, [2]], "w": [1, [3]]}), f"{RED}Correct {RESET}{RED}Correct {RESET}Close Close ")
        self.assertEqual(mastermind.getClues("rrbw", "rrrr", {"r": [2, [0, 1]], "o": [0, []], "y": [0, []], "g": [0, []], "b": [1, [2]], "w": [1, [3]]}), f"{RED}Correct {RESET}{RED}Correct {RESET}")  
        self.assertEqual(mastermind.getClues("bwrr", "rrrr", {"r": [2, [2, 3]], "o": [0, []], "y": [0, []], "g": [0, []], "b": [1, [0]], "w": [1, [1]]}), f"{RED}Correct {RESET}{RED}Correct {RESET}")  
        self.assertEqual(mastermind.getClues("rbwr", "rrrr", {"r": [2, [0, 3]], "o": [0, []], "y": [0, []], "g": [0, []], "b": [1, [1]], "w": [1, [2]]}), f"{RED}Correct {RESET}{RED}Correct {RESET}")  
        self.assertEqual(mastermind.getClues("brwr", "rrrr", {"r": [2, [1, 3]], "o": [0, []], "y": [0, []], "g": [0, []], "b": [1, [0]], "w": [1, [2]]}), f"{RED}Correct {RESET}{RED}Correct {RESET}")  

    def testIsColour(self):
        self.assertTrue(mastermind.isColour("rgbw"))
        self.assertFalse(mastermind.isColour("rtgb"))
        self.assertFalse(mastermind.isColour("@rgb"))
    
    def testGenCombo(self):
        self.assertTrue(len(mastermind.genCombo()[0])==4)

    
    def testSortLeader(self):
        self.assertEqual(sortLeader((3, "Jonah")), [(2, "sofia"), (3, "Peyton"), (3, "Jonah"),(4, "Scarlett")])
        self.assertEqual(sortLeader((2, "Jonah")), [(2, "sofia"), (2, "Jonah"), (3, "Peyton"), (3, "Jonah"),(4, "Scarlett")])

if __name__ == '__main__':
    unittest.main()