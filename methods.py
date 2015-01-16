import time

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
    #prints text, prints a blank line, waits half a sec

def ask(q,keepCase = False):
    v = input(q + " ")
    if keepCase == False:
        v = v.upper()
    return v
    #should ask a question, then return the response

def options(*o,menu=True):
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
            showMenu()
            text("Exited menu")
        elif choice == "MENU" and not menu:
            text("You can't access the menu at this time")
        elif match == 1:
            return choice
        else:
            text("Invalid option")
        
    #displays a list of preformatted options. o is a list of strings, menu
    #    is boolean, and determines whether the player can access the menu from
    #    that set of options. menu must be specified explicitly.
    #if the input is MENU, shows the menu
    #if the input matches an option
    #if the input does not match an option, forces user to pick again
    #usage: "choice = options("CHOICE 1", "CHOICE 2", ... , menu=False)

def showMenu():
    print("==========")
    print("   MENU   ")
    print("==========")
    b(1)
    print("Name:",you.name)
    print("Money: $" + str(you.money))
    print("Level:", you.level)
    print("Experience:", str(you.exp) + "/" + str(you.expNextLevel))
    print("Health:", str(you.health) + "/" + str(you.maxHealth))
    print("Strength:", you.strength, "- The damage you deal with physical weapons\
(fists, swords, etc.)")
    print("Defense:", you.defense, "- The amount of damage you resist.")
    print("Dexterity:", you.dexterity, "- The damage you deal with ranged weapons\
(guns, bows, etc.)")
    print("Crit Chance:", str(int(you.critChance * 100)) + "%", "- Chance that\
 your basic attacks will land a critical hit (x3 Damage)")
    b(1)
    while True:
        print("Options:")
        print("  - INV - Opens Inventory")
        print("  - RENAME - Pick a new name")
        print("  - EXIT - Closes Menu")
        choice = input("Choose an option: ").upper()
        if choice == "INV":
            text("Inventory not yet implemented")
            #run inventory function
        elif choice == "RENAME":
            you.rename()
            #run rename function
        elif choice == "EXIT":
            #choose = False
            break
        else:
            text("Invalid menu input")
