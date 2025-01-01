import chess
import glob
import re
from os import system, name

#Limit how much of each PGN is read. Set to -1 for no limit. (May result in incomplete games)
perFileLimit = -1

#Path to PGN files
PGNPath = r'PGNs/*.pgn'
PGNFiles = glob.glob(PGNPath)

PGNGames = [""]
i=0
j=0
next = False

#Read the PGN files
print("Reading all PGN files . . .")
for file in PGNFiles:
    #Iterate through PGN file's lines
    print("Reading " + file)
    try:
        with open(file, 'r') as f:
            game = ""
            for line in f:
                l = line.strip()
                
                if not " 2." in l:
                    continue
                    
                PGNGames.append(l)
                
                if j % 10000 == 0 and j != 0:
                    print(j, "Completed")
                #Limit number of lines searched
                if perFileLimit != -1 and j > perFileLimit:
                    j=0
                    break
                j += 1
            j = 0
    except:
        print("UTF encoding error, skipping file.")
        continue

print("Total of " + str(len(PGNGames)) + " games")
print("Elimnating duplicates . . .")
PGNGames = list(set(PGNGames))
        
#Parse games into UCI and write to file
print("Parsing to UCI & writing to file . . .")
f = open("UCI.txt", "a")
counter=0
skipped = 0
skip = False
for PGNGame in PGNGames:
    board = chess.Board()
    #Get rid of move numbers
    for i in range(0,15):
        PGNGame = PGNGame.replace(" " + str(i) + ".", " ")
    for i in range(0,15):
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
            skip = True
            break
    if skip:
        skip = False
        continue
    f.write(UCIGame + "\n") #Write move to file
    counter+=1

    #Occasionally print how many games written
    if counter % 10000 == 0:
        print(str(counter) + "/" + str(len(PGNGames)) + " Games parsed & written")

f.close()
print(str(len(PGNGames)-skipped), " Games completed,", skipped, " games skipped.\nPress enter to exit.")
pause=input()