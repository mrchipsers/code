RED = "\x1b[38;2;232;45;45m" 
CORRECTRED = "\x1b[38;2;255;0;0m"
ORANGE = "\x1b[38;2;255;127;0m"
YELLOW = "\x1b[38;2;223;223;40m" 
GREEN = "\x1b[38;2;71;211;71m" 
BLUE = "\x1b[38;2;0;149;255m" 
WHITE = "\x1b[38;2;255;255;255m" 
BLACK = "\x1b[38;2;0;0;0m" 
RESET = "\x1b[0m"

#leaderboardPath='leaderboard.txt' #this is for normal computers
leaderboardPath ='python/mastermind/leaderboard.txt' #my computer is messed up

with open(leaderboardPath, 'r') as f:
    leaderboard = []
    for i, line in enumerate(f.readlines()):
        line = line.split()
        leaderboard.append(line)

def sortLeader(new: list):
    for i, pos in enumerate(leaderboard):
        if pos[0] > new[0]:
            leaderboard.insert(i, [f"{int(new[0])+1}", new[1]])
            return
    leaderboard.append(new)
    
def saveLeader():  
    with open(leaderboardPath, 'w') as f:    
        for entry in leaderboard:
            f.write(f"{entry[0]} {entry[1]}\n")

def printLeader(max: int):
    print("posistion  guesses  name")
    for i in range(min(max, len(leaderboard))):
        print(f"{i+1:<11}{leaderboard[i][0]:9}{leaderboard[i][1]}")

sortLeader(["2", "sarah"])

printLeader(100)
printLeader(3)
saveLeader()
#print(concatClues(2,0))