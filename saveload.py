# Methods that handle saving and loading files

from methods import text, options, ask
from glob import glob
import os
# from math import sum
from ast import literal_eval

def saveGame(player, chapter):
    # Display quick player stats
    print("Name: " + player.name)
    print("Level: " + str(player.level))
    print("Money: " + str(player.money))
    text("Chapter: " + str(chapter))
    
    # Ask if the player wants to save, if not, confirm, then return if they REALLY don't want to save
    while True:
        print("Save your game?")
        saveChoice = options(player,["Y","N"],menu=False)
        if saveChoice == "N":
            print("Are you sure you don't want to save? All progress will be lost when you quit or die.")
            confirmChoice = options(player,["Y","N"],menu=False)
            if confirmChoice == "Y":
                text("You got it, chief. Saving skipped.")
                return
        else:
            break
    
    # Now that we know the player wants to save, name their save file
    # script_path = os.path.abspath(__file__) # i.e. /path/to/dir/foobar.py
    # script_dir = os.path.split(script_path)[0] #i.e. /path/to/dir/
    # rel_path = "saves/*.sav"
    # abs_file_path = os.path.join(script_dir, rel_path)
    foundFile = False
    while True:
        filename = "saves\\" + ask("Choose a name for your save file",keepCase=True) + ".sav"
        for fname in glob("saves/*.sav"):
            print(fname)
            if fname == filename:
                foundFile = True
                break
        if foundFile:
            print("That file already exists. Overwrite?")
            overwriteChoice = options(player,["Y","N"],menu=False)
            if overwriteChoice == "N":
                continue
            else:
                break
        else:
            break
    saveFile = open(filename,"w")
    print("Saving...")
    saveFile.write(str(chapter) + "\n")
    saveFile.write(player.name + "\n")
    print("." * 1)
    saveFile.write(str(player.money) + "\n")
    print("." * 2)
    saveFile.write(str(player.level) + "\n")
    print("." * 3)
    saveFile.write(str(player.strength) + "\n")
    print("." * 4)
    saveFile.write(str(player.dexterity) + "\n")
    print("." * 5)
    saveFile.write(str(player.exp) + "\n")
    print("." * 4)
    saveFile.write(str(player.health) + "\n")
    print("." * 3)
    saveFile.write(str(player.items) + "\n")
    print("." * 2)
    saveFile.write(str(player.equipment) + "\n")
    print("." * 1)
    saveFile.write(str(player.specials) + "\n")
    saveFile.write(str(player.specialPoints) + "\n")
    saveFile.close()
    text("Saving complete!")
        
def loadGame(player):
    files = []
    for fname in glob("saves/*.sav"):
        files.append(fname)
    if not files:
        text("No save files found, so there's nothing to load. Sorry!")
        return 0
    for f in files:
        print("before",f)
        ind = files.index(f)
        f = f.split(".")[0]
        f = f.split("\\")[1]
        files[ind] = f
        print("after",f)
    print("Choose a file to load:")
    fileChoice = options(player,files,menu=False)
    loadFile = open("saves\\" + fileChoice + ".sav")
    stats = []
    for line in loadFile:
        stats.append(line.replace("\r",""))
    chapter = eval(stats[0])
    player.name = stats[1].replace("\n","")
    player.money = eval(stats[2])
    player.level = eval(stats[3])
    player.expNextLevel = 5 * 2 ** (player.level - 1)
    player.critChance = 0.01 + int(sum(range(2,player.level))) * 0.01
    player.maxSpecialPoints = 2 + player.level
    player.maxHealth = 10 + sum(range(2,player.level))
    player.defense = (player.level - 1) // 2
    player.strength = eval(stats[4])
    player.dexterity = eval(stats[5])
    player.exp = eval(stats[6])
    player.health = eval(stats[7])
    player.items = literal_eval(stats[8])
    player.equipment = literal_eval(stats[9])
    player.specials = literal_eval(stats[10])
    player.specialPoints = eval(stats[11])
    text("Game loaded! Welcome back, " + player.name + "!")
    loadFile.close()
    return chapter