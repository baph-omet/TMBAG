import time
from items import *
# from actors import *
from items import *

#Custom Functions
def w(i):
    time.sleep(i)
    # shortcut for sleep
    
def b(i):
    for f in range(i):
        print()
    # prints i number of blank lines
    
def text(t):
    print(t)
    b(1)
    w(1)
    input("")
    # prints text, prints a blank line, waits half a sec
    # The input makes it so that players have to hit enter to advance text
    # It's crude, but it works.

def ask(q,keepCase = False):
    v = input(q + " ")
    if keepCase == False:
        v = v.upper()
    return v
    #should ask a question, then return the response

def options(player,*o,menu=True):
    while True:
        print("Options:")
        match = 0
        for s in o:
            print("  -",str(s).upper())
        choice = ask("What will you do?")
        for s in o:
            if choice == str(s).upper():
                match = 1
        if choice == "MENU" and menu:
            showMenu(player)
            text("Exited menu")
        elif choice == "MENU" and not menu:
            text("You can't access the menu at this time")
        elif match == 1:
            b(1)
            return choice
        else:
            text("Invalid option")
            
    # displays a list of preformatted options. o is a list of strings, menu
    #     is boolean, and determines whether the player can access the menu from
    #     that set of options. menu must be specified explicitly.
    # if the input is MENU, shows the menu
    # if the input matches an option
    # if the input does not match an option, forces user to pick again
    # usage: "choice = options("CHOICE 1", "CHOICE 2", ... , menu=False)
    
def showInventory(player):
    print("=============")
    print("  INVENTORY")
    print("=============")
    b(1)
    print("===========")
    print(" EQUIPMENT")
    print("===========")
    print("|")
    if player.equipment[0] == "":
        print("| Weapon: FISTS")
    else:
        print("| Weapon:",player.equipment[0].name)
    if player.equipment[1] == "":
        print("| Headgear: NONE")
    else:
        print("| Headgear:",player.equipment[1].name)
    if player.equipment[2] == "":
        print("| Armor: NONE")
    else:
        print("| Armor:",player.equipment[2].name)
    if player.equipment[3] == "":
        print("| Footgear: NONE")
    else:
        print("| Footgear:",player.equipment[3].name)
    b(1)
    print("=======")
    print(" ITEMS")
    print("=======")
    b(1)
    for k,v in player.items:
        if v > 0:
            print("|",k.name,"x" + str(v))
    for k,v in player.unequipped:
        if v > 0:
            print("|",k.name,"x" + str(v))
    while True:
        print("Options:")
        print("  - USE - Use an item or equip equipment")
        print("  - UNEQUIP - Unequip equipment")
        print("  - TOSS - Throw an item away")
        print("  - EXIT - Close Inventory")
        choice = input("Choose an option: ").upper()
        if choice == "USE":
            pass
        elif choice == "UNEQUIP":
            pass
        elif choice == "TOSS":
            pass
        elif choice == "EXIT":
            break
        else:
            text("Invalid input")

def showMenu(player):
    print("==========")
    print("   MENU   ")
    print("==========")
    b(1)
    print("Name:",player.name)
    print("Money: $" + str(player.money))
    print("Level:", player.level)
    print("Experience:", str(player.exp) + "/" + str(player.expNextLevel))
    print("Health:", str(player.health) + "/" + str(player.maxHealth))
    print("Strength:", player.strength, "- The damage you deal with physical weapons\
(fists, swords, etc.)")
    print("Defense:", player.defense, "- The amount of damage you resist.")
    print("Dexterity:", player.dexterity, "- The damage you deal with ranged weapons\
(guns, bows, etc.)")
    print("Crit Chance:", str(int(player.critChance * 100)) + "%", "- Chance that\
 your basic attacks will land a critical hit (x3 Damage)")
    b(1)
    while True:
        print("Options:")
        print("  - INV - Open Inventory")
        print("  - RENAME - Pick a new name")
        print("  - EXIT - Close Menu")
        print("  - QUIT - Quit the game")
        choice = input("Choose an option: ").upper()
        if choice == "INV":
            showInventory(player)
            #run inventory function
        elif choice == "RENAME":
            player.rename()
            #run rename function
        elif choice == "EXIT":
            #choose = False
            break
        elif choice == "QUIT":
            if input("Type Y if you're sure you want to quit.\n(Progress will not be saved!): ").upper() == "Y":
                print("See you later!")
                quit()
        else:
            text("Invalid menu input")