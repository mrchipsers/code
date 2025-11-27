RED = "\x1b[38;2;232;45;45m" #colorama.Fore.RED
CORRECTRED = "\x1b[38;2;255;0;0m"
ORANGE = "\x1b[38;2;255;127;0m"
YELLOW = "\x1b[38;2;223;223;40m" #colorama.Fore.YELLOW
GREEN = "\x1b[38;2;71;211;71m" #colorama.Fore.GREEN
BLUE = "\x1b[38;2;0;149;255m" #colorama.Fore.BLUE
WHITE = "\x1b[38;2;255;255;255m" #colorama.Fore.WHITE
BLACK = "\x1b[38;2;0;0;0m" #colorama.Fore.BLACK
RESET = "\x1b[0m" #colorama.Style.RESET_ALL

#leaderboardPath='leaderboard.txt' #this is for normal computers
leaderboardPath='python/mastermind/leaderboard.txt' #my computer is messed up

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
    print("posistion   guesses    name")
    for i, pos in enumerate(leaderboard):
        if i==max:
            break
        print(f"{i+1}{" "*(12-len(f"{i+1}"))}{pos[0]}{" "*(11-len(pos[0]))}{pos[1]}")

sortLeader(["2", "sarah"])

printLeader(200)
saveLeader()
#print(concatClues(2,0))