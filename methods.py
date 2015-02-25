import time

import items

#Custom Functions
# shortcut for sleep
def w(i):
    time.sleep(i)
    
# prints i number of blank lines
def b(i):
    for f in range(i):
        print()
    
# prints text, prints a blank line, waits half a sec
# The input makes it so that players have to hit enter to advance text
# It's crude, but it works.
def text(t):
    print(t)
    b(1)
    # w(1)
    input("")

#should ask a question, then return the response
def ask(q,keepCase = False):
    while True:
        v = input(q + " ")
        if v:
            if keepCase == False:
                v = v.upper()
            return v

# displays a list of preformatted options. o is a list of strings, menu
#     is boolean, and determines whether the player can access the menu from
#     that set of options. menu must be specified explicitly.
# if the input is MENU, shows the menu
# if the input matches an option
# if the input does not match an option, forces user to pick again
# usage: "choice = options(you,["CHOICE 1", "CHOICE 2", ... ], menu=False)
def options(player,o,menu=True):
    while True:
        print("Options:")
        match = 0
        for s in o:
            print("  -",str(s).upper())
        choice = ask("Choose an option:")
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
    
def showInventory(player):
    closeInv = False
    while not closeInv:
        print("=============")
        print("  INVENTORY")
        print("=============")
        b(1)
        print("===========")
        print(" EQUIPMENT")
        print("===========")
        print("|")
        debug = False
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
        print("|")
        if not player.items:
            print("| No items")
        else:
            for k in player.items:
                if player.items[k] > 0:
                    for i in items.Consumable.__subclasses__():
                        if k == i.name:
                            itemDesc = i.desc
                            break
                    else:
                        for i in items.Equipment.__subclasses__():
                            if k == i.name:
                                itemDesc = i.desc
                                break
                    print("| " + k + " x" + str(player.items[k]) + " - " + itemDesc)
        b(1)
        
        while True:
            print("Options:")
            print("  - USE - Use an item or equip equipment")
            print("  - UNEQUIP - Unequip equipment")
            print("  - TOSS - Throw an item away")
            if debug:
                print("  - GIVE - Give the player an item")
            print("  - EXIT - Close Inventory")
            
            choice = input("Choose an option: ").upper()
            b(1)
            if choice == "USE":
                itemChoice = player.itemChoose()
                if itemChoice:
                    player.itemEffect(itemChoice)
                
            elif choice == "UNEQUIP":
                done = False
                while not done:
                    foundItem = False
                    for e in player.equipment:
                        if e:
                            print("  - " + e.name + " - " + e.desc)
                            foundItem = True
                    if not foundItem:
                        text("You have nothing equipped.")
                        break
                    else:
                        unequipChoice = input("Choose an item to unequip: ")
                        for e in player.equipment:
                            if e and unequipChoice.upper() == e.name:
                                player.unequip(e)
                                done = True
                                break
                        else:
                            text("Invalid input")
                        if done:
                            break
                    
                
            elif choice == "TOSS":
                itemChoice = player.itemChoose()
                if itemChoice:
                    player.toss(itemChoice)
                
            elif choice == "DEBUG":
                debug = not debug
                
            elif choice == "GIVE":
                itemChoice = []
                for i in items.Consumable.__subclasses__():
                    itemChoice.append(i.name)
                for i in items.Equipment.__subclasses__():
                    itemChoice.append(i.name)
                player.giveItem(options(player,itemChoice))
                
            elif choice == "EXIT":
                closeInv = True
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
    print("Special Points:",str(player.specialPoints) + "/" + str(player.maxSpecialPoints))
    print("Strength:", player.strength, "- The damage you deal with physical weapons (fists, swords, etc.)")
    print("Defense:", player.defense, "- The amount of damage you resist.")
    print("Dexterity:", player.dexterity, "- The damage you deal with ranged weapons (guns, bows, etc.)")
    print("Crit Chance:", str(int(player.critChance * 100)) + "%", "- Chance that\
 your basic attacks will land a critical hit (x3 Damage)")
    b(1)
    while True:
        print("Options:")
        print("  - INV - Open Inventory")
        print("  - RENAME - Pick a new name")
        print("  - SPECIALS - Check special moves")
        print("  - EXIT - Close Menu")
        print("  - QUIT - Quit the game")
        choice = input("Choose an option: ").upper()
        if choice == "INV":
            showInventory(player)
            #run inventory function
        elif choice == "RENAME":
            player.rename()
            #run rename function
        elif choice == "SPECIALS":
            showSpecials(player)
            # show player's specials
        elif choice == "EXIT":
            break
        elif choice == "QUIT":
            if input("Type Y if you're sure you want to quit.\n(Progress WILL NOT be saved!): ").upper() == "Y":
                print("See you later!")
                quit()
        else:
            text("Invalid menu input")
            
def showSpecials(player):
    b(3)
    print("=========")
    print(" SPECIAL ")
    print("  MOVES  ")
    print("=========")
    b(1)
    print("===")
    print("|")
    if player.specials:
        for s in player.specials:
            print("| - (" + str(s.specialPointCost) + ") " + str(s.name) + " - " + s.desc)
    else:
        print("| You haven't learned any specials!")
    print("|")
    print("===")
    b(3)
    input("Press ENTER to return to MENU")
    b(3)