import chess
import glob
import re
from os import system, name

#Limit how much of each PGN is read. Set to -1 for no limit. (May result in incomplete games)
perFileLimit = 50000

#Path to PGN files
PGNPath = r'PGNs/*.pgn'
PGNFiles = glob.glob(PGNPath)

PGNs = [""]
i=0
j=0

#Read the PGN files
print("Reading all PGN files . . .")
for file in PGNFiles:
    #Iterate through PGN file's lines
    print("Reading " + file)
    with open(file, 'r') as f:
        for line in f:
            l = line.strip()
            #Skip line if it isn't moves
            if "[" in l or l == "":
                continue

            PGNs[i] += l + " " #Add moves to list
            if j % 10000 == 0:
                print(j, "Completed")
            #Limit number of lines searched
            if perFileLimit != -1 and j > perFileLimit:
                j=0
                break
            j += 1
        i += 1
        j = 0
        PGNs.append("")
PGNs.pop()
PGNGames = []

#Split the games in each PGN file
print("Splitting games . . .")
for game in PGNs:
    delimiters = ["0-1", "1-0", "1/2-1/2", "*"] #Games are split by their result
    pattern = r'\b(?:' + '|'.join(map(re.escape, delimiters)) + r')\b'
    result = re.split(pattern, game)
    result = [segment.strip() for segment in result if segment.strip()]
    for i in result:
        PGNGames.append(i)
print("Total of " + str(len(PGNGames)) + " games")

#Parse games into UCI and write to file
print("Parsing to UCI & writing to file . . .")
f = open("UCI.txt", "a")
counter=0
skipped = 0
for PGNGame in PGNGames:
    board = chess.Board()

    #Get rid of move numbers
    for i in range(0,200):
        PGNGame = PGNGame.replace(" " + str(i) + ".", " ")
    for i in range(0,200):
        PGNGame = PGNGame.replace(str(i) + ".", "")

    PGNGame = PGNGame.split()#Split game into individual moves

    #Convert move to UCI
    UCIGame=""
    for move in PGNGame:

        #Occasionally games cannot be parsed.
        try:
            UCIGame += board.push_san(move).uci() + " "
        except:
            skipped += 1
            print("Error parsing game")
            print(PGNGame)
            break

    f.write(UCIGame + "\n") #Write move to file
    counter+=1

    #Occasionally print how many games written
    if counter % 10000 == 0:
        print(str(counter) + "/" + str(len(PGNGames)) + " Games parsed & written")

f.close()
print(str(len(PGNGames)-skipped), " Games completed,", skipped, " games skipped.\nPress enter to exit.")
pause=input()