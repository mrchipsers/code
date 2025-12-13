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

leaderboardPath="leaderboard.txt" #this is for normal computers


def openLeader():
    with open(leaderboardPath, 'r') as f:
        leaderboard = []
        for line in f.readlines():
            line = line.split()
            leaderboard.append(line)
    return leaderboard

def sortLeader(name: str, num: str, leaderboard: list):
    for i, pos in enumerate(leaderboard):
        if pos[0] > num:
            leaderboard.insert(i, [f"{int(num)+1}", name])
            return i
    leaderboard.append([num, name])
    return len(leaderboard)-1
    
def saveLeader(leaderboard: list):  
    with open(leaderboardPath, 'w') as f:    
        for entry in leaderboard:
            f.write(f"{entry[0]} {entry[1]}\n")

def printLeader(max: int, leaderboard: list, you: int):
    print("posistion  guesses  name")
    for i in range(min(max, len(leaderboard))):
        if i==you:
            print(f"{PURPLE}{i+1:<11}{leaderboard[i][0]:9}{leaderboard[i][1]}{RESET}")
        else:    
            print(f"{i+1:<11}{leaderboard[i][0]:9}{leaderboard[i][1]}")

leaderboard = openLeader()
pos = sortLeader("sarah", "2", leaderboard)
printLeader(100, leaderboard, pos)
saveLeader(leaderboard)