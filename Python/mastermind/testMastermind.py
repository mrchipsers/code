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
        self.assertEqual(mastermind.getClues("rgbw", "yoyo"), f"{BLACK}None{RESET}") 
        self.assertEqual(mastermind.getClues("rgbw", "rgbw"), "Congratulations! Your guess is correct!")
        self.assertEqual(mastermind.getClues("rgbw", "rgwb"), f"{RED}Correct {RESET}{RED}Correct {RESET}Close Close ") 

    def testIsColour(self):
        self.assertTrue(mastermind.isColour("rgbw"))
        self.assertFalse(mastermind.isColour("rtgb"))
        self.assertFalse(mastermind.isColour("@rgb"))
    
    def testGenCombo(self):
        self.assertTrue(len(mastermind.genCombo())==4)

    
    def testSortLeader(self):
        self.assertEqual(sortLeader((3, "Jonah")), [(2, "sofia"), (3, "Peyton"), (3, "Jonah"),(4, "Scarlett")])
        self.assertEqual(sortLeader((2, "Jonah")), [(2, "sofia"), (2, "Jonah"), (3, "Peyton"), (3, "Jonah"),(4, "Scarlett")])

if __name__ == '__main__':
    unittest.main()