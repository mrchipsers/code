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
leaderboardPath='Python/mastermind/leaderboard.txt' #my computer is messed up

with open(leaderboardPath, 'r') as f:
    leaderboard = []
    for i, line in enumerate(f.readlines()):
        line.replace('\n','')
        line = line.split()
        leaderboard.append(line)

def sortLeader(entry: list):
    for i, pos in enumerate(leaderboard):
        if pos[0] > entry[0]:
            leaderboard.insert(i, entry)
            return
    leaderboard.append(entry)

def saveLeader():
    with open(leaderboardPath, 'w') as f:
        for entry in leaderboard:
            guesses = entry[0]
            name = entry[1]
            f.write(f"{guesses} {name}\n")

def printLeader(max: int):
    print("posistion  guesses    name")
    for i, pos in enumerate(leaderboard):
        guesses = pos[0]
        name = pos[1]
        if i==max:
            break
        print(f"{i+1}{" "*(12-len(f"{i+1}"))}{guesses}{" "*(11-len(guesses))}{name}")

def concatClues(countAt: int, countClose: int):
    return (f"{CORRECTRED}{"Correct "*countAt}{RESET}")+(f"{WHITE}{"Close "*countClose}{RESET}")


#printLeader(10)
print(concatClues(2,0))