import chess
import glob
import re
from os import system, name

#Limit how much of each PGN is read. Set to -1 for no limit.
perFileLimit = 15000


PGNPath = r'PGNs/*.pgn'
PGNFiles = glob.glob(PGNPath)
PGNs = [""]
i=0
j=0
print("Reading All PGN Files")
for file in PGNFiles:
    print("Reading " + file)
    with open(file, 'r') as f:
        for line in f:
            if "[" in line.strip() or line.strip() == "":
                continue
            PGNs[i] += line.strip() + " "
            if j % 1000 == 0:
                pass
                #print(j, " Lines Parsed")
            if perFileLimit != -1 and j > perFileLimit:
                j=0
                break
            j += 1
        i += 1
        PGNs.append("")
PGNs.pop()
PGNGames = []

print("Parsing games")
for game in PGNs:
    delimiters = ["0-1", "1-0", "1/2-1/2", "*"]
    pattern = r'\b(?:' + '|'.join(map(re.escape, delimiters)) + r')\b'
    result = re.split(pattern, game)
    result = [segment.strip() for segment in result if segment.strip()]
    for i in result:
        PGNGames.append(i)
f = open("UCI.txt", "a")
counter=0
print("Total of " + str(len(PGNGames)) + " Games")
for PGNGame in PGNGames:
    board = chess.Board()
    PGNGame = PGNGame.replace("0-1", "")
    PGNGame = PGNGame.replace("1-0", "")
    PGNGame = PGNGame.replace("1/2-1/2", "")
    for i in range(0,200):
        PGNGame = PGNGame.replace(" " + str(i) + ".", " ")
    for i in range(0,200):
        PGNGame = PGNGame.replace(str(i) + ".", "")
    PGNGame = PGNGame.split()
    UCIGame=""
    for move in PGNGame:
        try:
            UCIGame += board.push_san(move).uci() + " "
        except:
            print("Error parsing game")
            print(PGNGame)
            break
    f.write(UCIGame + "\n")
    counter+=1
    if counter % 10000 == 0:
        print(str(counter) + "/" + str(len(PGNGames)) + " Games Added")
print("Complete")
f.close()
pause=input()