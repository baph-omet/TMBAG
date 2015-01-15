#AWW YISS MOTHA FUKKIN IMPORTS
import time
import random

#SOME CUSTOM FUNCTIONS UP IN THIS BITCH
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
            print("  -",s.upper())
        choice = ask("What will you do?")
        for s in o:
            if choice == s.upper():
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

#Battle Engine
def battle(*enemies):
    #enemies is a list of enemy objects, not strings
    turn = 0
    guarding = False
    print("=" * 5)
    print("=" * 4)
    print("=" * 3)
    print("=" * 4)
    print("=" * 5)
    print("=" * 4)
    print("=" * 3)
    print("=" * 4)
    print("=" * 5)
    print("=" * 6)
    print("=" * 7)
    print("=" * 8)
    print("=" * 9)
    print("=" * 10)
    print("=" * 11)
    print("| BATTLE! |")
    print("=" * 11)
    b(1)
    while True:
        #print player stats
        print("*" * 12)
        print("|" + " " * int((10 - len(you.name))/2) + you.name + " " * \
              int((10 - len(you.name))/2) + "|")
        print("| HP: " + str(you.health) + "/" + str(you.maxHealth))
        print("*" * 12)
        b(2)
        print("=" * 24)
        b(2)

        #If there are multiple enemies, number them
        n = 1
        numberedEnemies = []
        for i in enemies:
            numberedEnemies.append(str(i) + " " + str(n))
            n += 1
            
        #print enemy stats
        for i in enemies:
            if len(enemies) > 1:
                enemyNumber = str(enemies.index(i) + 1)
            else:
                enemyNumber = ""
            print("*" * 12)
            print("|" + " " * int((8 - len(i.Name))/2) + i.Name\
                + Number  + " " * int((8 - len(i.Name))/2) + "|")
            print("| HP: " + str(i.Health) + "/" + str(i.MaxHealth))
            print("*" * 12)

        if guarding:
            guarding = False
            text("You are no longer defending")

        #Choose a battle command
        while True:
            battleChoice = options("ATTACK","SPECIAL","DEFEND","ITEM","MENU","RUN")
            if battleChoice == "ATTACK":
                #select a target
                if len(enemies) > 1:
                    print("Pick a Target:")
                    target = enemies[options(range(len(numberedEnemies)))-1]
                else:
                    target = enemies[0]
                #do an attack
                    
            elif battleChoice == "SPECIAL":
                pass
            elif battleChoice == "DEFEND":
                pass
            elif battleChoice == "ITEM":
                pass
            elif battleChoice == "RUN":
                pass
        

#Class definitions
##Player definition
class Player:
    def __init__(self,playerName):
        self.name = playerName
        self.money = 0
        self.level = 1
        self.exp = 0
        self.expNextLevel = 5
        self.health = 20
        self.maxHealth = 20
        self.strength = 1
        self.defense = 0
        self.dexterity = 1
        self.accuracy = 0.95
        self.critChance = 0.05
    def rename(self):
        text("It's at this point in your adventure that you decide to forge a new\
     itentity for yourself. You're the boss. Who's to tell you what your name is?")
        self.name = input("What shall your new name be? ")
        text("You are now known as " + self.name + ", a name certainly 100, nay, 1000 times\
     the superior of your old monicker.")
        # renames the player

    def attack(self, target):
        damage = self.strength - target.defense
        target.health -= damage
        #attacks the target
    def defend(self):
        if 

##Enemy definitions
class Enemy:
    def __init__(self):
        self.name = "Dummy"
        self.desc = "You forgot to set the defaults for this enemy type."
        self.strength = 1
        self.defense = 0
        self.health = 5
        self.maxHealth = 5
        self.expYield = 1
        self.items = []
        self.specials = []
        self.attackChance = 1
        self.defendChance = 0
        self.itemChance = 0
        self.specialChance = 0
        self.accuracy = 1
        self.CritChance = 0
    def attack(self):
        damage = self.Strength - you.defense
        text(self.name + " attacked you for " + str(damage))
        you.health -= damage
        # attacks the player
    def defend(self):
        print("Enemy defending not yet implemented")
    def item(self):
        print("Enemy item use not yet implemented")
    def special(self):
        print("Enemy special attacks not yet implemented")
    def crit(self):
        print("Enemy criticals not yet implemented")
        
    ''' Varible definitions:

        # Stats
        name = display name of enemy, shown in battle (string)
        desc = description of enemy, shown when enemy is examined
           in battle (string)
        strength = raw hit point damage from enemy attacks (int)
        defense = hit points absorbed by enemy (int)
        health = current health of enemy, modifed during battle (int)
        maxHealth = maximum health of enemy, not modified during battle
           (int)
        expYield = experience given for defeating this enemy (int)
           
        # Items/Specials
        items = list of items held by enemy (list of strings)
        specials = list of special moves usable by enemy (list of strings)
        
        # Behavior
        ## Choices(total probability should add to 1)
        attackChance = probability that the enemy will use its standard
            attack (int from 0 to 1)
        defendChance = probability that the enemy will defend (int from
            0 to 1)
        itemChance = probability that the enemy will use an item. All
            items have equal weight for now (int from 0 to 1)
        specialChance = probability that the enemy will use a special move.
            (int from 0 to 1)

        ## Chances (probabilities are independent)
        accuracy = probability that a standard attack will hit (int from
            0 to 1) (calculated separately from above probabilities)
        critChance = probability that an enemy will land a critical hit
            for x3 damage (int from 0 to 1)
    '''

class Guard(Enemy):
    def __init__(self):
        self.name = "Guard"
        self.sesc = "An alien guard. Blueish-gray skin, four deep, black eyes.\
     Carries a spear."
        self.strength = 1
        self.defense = 0
        self.health = 5
        self.maxHealth = 5
        self.expYield = 1
        self.items = []
        self.specials = []
        self.attackChance = 0.8
        self.defendChance = 0.2
        self.itemChance = 0
        self.specialChance = 0
        self.accuracy = 0.8
        self.critChance = 0.01

#########################################################################
#                           Game starts here                            #
#########################################################################
# GAME CHAPTERS
## CHAPTER 1
def ChapterOne():
    choice = ""
    text("**********")
    text("*********")
    text("********")
    text("*******")
    text("******")
    text("*****")
    text("****")
    text("***")
    text("**")
    text("*")

    #
    text("For a while, everything is black. Before too long, you begin to slip back\
     into consciousness. You find yourself sprawled on the cold floor of a sterile,\
     white room. Bright lights from the ceiling hurt your head as you struggle with\
     the slippery grasp of consciousness.")
    text("You are finally awoken by the feeling of the floor rumbling beneath you.\
     you sit up slowly. There is a door immediately in front of you.")
    while True:
        choice = options("EXAMINE ROOM","TRY DOOR")
        if choice == "EXAMINE ROOM" and you.money == 0:
            text("The room is square as can be, the floor, walls, and ceiling made up of\
     of white panels. There are no windows. The floors seem to be completely bare.")
            text("Actually, it looks like there's something in the corner of the room\
    . It looks like... some money?")
            text("You find $3! Alright.")
            you.money += 3
        elif choice == "EXAMINE ROOM":
            text("There doesn't seem to be anything else here.")
        elif choice == "TRY DOOR":
            text("The door looks heavy and is cold to the touch. There doesn't seem to\
     be a handle, though. No matter what you try, the door doesn't open.")
            break
    text("It's at this time that you hear a pounding on the door. Before you have\
     time to react, the door bursts open. A strange-looking creature strides in.\
     It doesn't look friendly. It's making some weird noise at you and brandishing\
     a nasty-looking spear. Looks light it's trying to pick a fight.")

    guard = Guard()
    battle(guard)


#########################################################################
#                             TITLE SCREEN                              #
#########################################################################
print("********************")
print("This Might Be a Game")
print(" By Nate (iamvishnu)")
print("       v0.0.1       ")
print("********************")
w(3)
b(3)
print("+-+-+-+-+-+-+-+-+-+-+-+")
print("       MAIN MENU       ")
print("+-+-+-+-+-+-+-+-+-+-+-+")
b(1)
w(0.5)
while True:
    print("Options:")
    print("  - INFO")
    print("  - NEW")
    print("  - LOAD")
    print("  - EXIT")
    choice = input("Select an option: ").upper()
    if choice == "INFO":
        text("'This Might Be a Game' is an interactive story written in Python \
by Nate(iamvishnu). In this game, you follow along with a story, while \
providing input to various text prompts. Prompts are case-insensitive. \
Type MENU when presented with options to show the menu. Enjoy!")
    elif choice == "NEW":
        while True:
            nameChoice = str(input("What is your name, friend? "))
            if len(nameChoice) > 8:
                text("That's kind of a mouthful. How about something shorter?")
            else:
                break
        you = Player(nameChoice)
        text("Nice to meet you, " + you.name)
        text("Your story is about to begin.")
        i = 0
        while i < 1:
            ready = input("Are you ready to begin? (Y/N) ").upper()
            if ready == "N":
                text("You should probably quit now, then. The adventure ahead isn't for babies.")
            elif ready == "Y":
                text("That's the spirit! Let's get started, shall we?")
                i += 1
            else:
                text("Try again, smartass.")
        ChapterOne()
    elif choice == "LOAD":
        text("Loading games is not yet implemented. Sorry!")
    elif choice == "EXIT":
        quit()
    else:
        text("Invalid input")


        
        
