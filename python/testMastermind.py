import project
import unittest

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

class mastermindTest(unittest.TestCase):
    def testConcatClues(self):
        self.assertEqual(project.concatClues(2, 3), f"{CORRECTRED}Correct Correct {WHITE}Close Close Close {RESET}") 
        self.assertEqual(project.concatClues(0, 3), f"{CORRECTRED}{WHITE}Close Close Close {RESET}") 
        self.assertEqual(project.concatClues(2, 0), f"{CORRECTRED}Correct Correct {WHITE}{RESET}") 
        self.assertEqual(project.concatClues(0, 0), f"{CORRECTRED}{WHITE}{RESET}") 

    def testgetClues(self):
        self.assertEqual(project.getClues("rgbw", "yoyo"), f"{BLACK}None{RESET}") 
        self.assertEqual(project.getClues("rgbw", "rgbw"), "win")
        self.assertEqual(project.getClues("rgbw", "rgwb"), f"{CORRECTRED}Correct Correct {WHITE}Close Close {RESET}")
        self.assertEqual(project.getClues("ywrb", "wwrb"), f"{CORRECTRED}Correct Correct Correct {WHITE}{RESET}")
        self.assertEqual(project.getClues("rrbw", "rrrr"), f"{CORRECTRED}Correct Correct {WHITE}{RESET}")  
        self.assertEqual(project.getClues("bwrr", "rrrr"), f"{CORRECTRED}Correct Correct {WHITE}{RESET}")  
        self.assertEqual(project.getClues("brwr", "rooo"), f"{CORRECTRED}{WHITE}Close {RESET}")  
        self.assertEqual(project.getClues("brwr", "oroo"), f"{CORRECTRED}Correct {WHITE}{RESET}")    
        self.assertEqual(project.getClues("oygg", "rgrg"), f"{CORRECTRED}Correct {WHITE}Close {RESET}")
    
    def testIsColour(self):
        self.assertTrue(project.isColour("rgbw"))
        self.assertFalse(project.isColour("rtgb"))
        self.assertFalse(project.isColour("@rgb"))
        self.assertTrue(project.isColour(""))
    
    def testGenCombo(self):
        self.assertTrue(len(project.genCombo())==4)
        
    def testColourOutput(self):
        self.assertEqual(project.colourOutput("royg"), f"{RED}r{ORANGE}o{YELLOW}y{GREEN}g{RESET}")
    
    def testSortLeader(self):
        leaderboard = [["0", "Genius"], ["3", "Sarah"], ["DNF", "Idiot"]]
        number, name = ["2", "you"]
        dnf, idiot = ["DNF", "EvenDumberIdiot"]
        self.assertEqual(project.sortLeader(name, number, leaderboard), 1)
        self.assertEqual(leaderboard, [["0", "Genius"], ["3", "you"], ["3", "Sarah"], ["DNF", "Idiot"]])
        self.assertEqual(project.sortLeader(idiot, dnf, leaderboard), 4)
        self.assertEqual(leaderboard, [["0", "Genius"], ["3", "you"], ["3", "Sarah"], ["DNF", "Idiot"], ["DNF", "EvenDumberIdiot"]])

if __name__ == '__main__':
    unittest.main()