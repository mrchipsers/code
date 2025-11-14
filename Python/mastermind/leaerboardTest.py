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

printLeader(10)
