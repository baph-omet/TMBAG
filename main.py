#Imports
import time
import random

from methods import text, b, w, options
from saveload import saveGame, loadGame
from battle import battle
import actors
import enemies
import items

#########################################################################
#                           Game starts here                            #
#########################################################################
# GAME CHAPTERS
## CHAPTER 1
def ChapterOne(player):
    saveGame(player,1)
    print("*********")
    print("CHAPTER 1")
    print("*********")
    print("****")
    print("***")
    print("**")
    print("*")
    text("For a while, everything is black. Before too long, you begin to slip back\ninto consciousness. You find yourself sprawled on the cold floor of a sterile,\nwhite room. Bright lights from the ceiling hurt your head as you struggle with\nthe slippery grasp of consciousness.")
    text("You are finally awoken by the feeling of the floor rumbling beneath you.\nyou sit up slowly. There is a door immediately in front of you.")
    while True:
        choice = options(player,["EXAMINE ROOM","TRY DOOR"])
        if choice == "EXAMINE ROOM" and player.money == 0:
            text("The room is square as can be, the floor, walls, and ceiling made up of white panels.\nThere are no windows. The floors seem to be completely bare.")
            text("Actually, it looks like there's something in the corner of the room.\nIt looks like... some money?")
            text("You find $3! Alright.")
            player.money += 3
        elif choice == "EXAMINE ROOM":
            text("There doesn't seem to be anything else here.")
        elif choice == "TRY DOOR":
            text("The door looks heavy and is cold to the touch. There doesn't seem to\nbe a handle, though. No matter what you try, the door doesn't open.")
            break
    text("It's at this time that you hear a pounding on the door. Before you have\ntime to react, the door bursts open. A strange-looking creature strides in.\nIt doesn't look friendly. It's making some weird noise at you and brandishing\na nasty-looking spear. Looks light it's trying to pick a fight.")

    guardA = enemies.Guard()
    battle(player,[guardA])
    
    text("Well that sure was rude.")
    text("That guard that attacked you looked like some kind of alien.\nPerhaps you were abducted? At any rate, it looks\n like they left the door open. You decide not to hang around.")
    text("You find yourself in a long hallway. As you approach the end of\nthe hallway, you notice that the path branches off to the\nleft and right. Which path will you take?")
    
    choice = options(player,["LEFT","RIGHT"])
    if choice == "LEFT":
        text("You venture down the hallway to the left. The path makes multiple turns before ending in a door similar to the one in which you awoke.")
        text("The door slides open softly at your touch, revealing a small, dark room beyond.")
        text("You walk in cautiously, hoping not to get ambushed. It looks like this room is...\na broom closet. There's a BROOM and a BUCKET sitting nonchalant in the middle of the floor.")
        
        choice = options(player,["TAKE STUFF","LEAVE STUFF ALONE"])
        if choice == "TAKE STUFF":
            text("Hell yeah, free stuff. Why WOULDN'T you take it?")
            player.giveItem("BUCKET")
            player.giveItem("BROOM")
            text("You quickly scoop up the items and cram them into your extradimensional inventory.\nHow exactly does that work? Don't think about it too hard, kid.")
        else:
            text("That stuff just looks like junk. You know better than to clog up your inventory with junk.\nHas Bethesda taught you nothing?")
            
        text("Boy that sure was a fun diversion. Now that you've conquered the broom closet, you decide\nto go back the way you came and take the right path.")
    
    text("The hallway to the right runs for about 200 feet before opening up into\na large room. Large glass vats are laid out in a grid across the floor,\nfilled with some sort of green ooze. On the other side of the room,\nyou can hear the sound of footsteps. What do you do?")
    
    choice = options(player,["SNEAK PAST","FIGHT"])
    sneakChance = random.random()
    guardA = enemies.Guard()
    guardB = enemies.Guard()
    if choice == "SNEAK PAST":
        if sneakChance > 0.5:
            text("You manage to sneak past the guards as they walk by. You're feeling pretty good about yourself.")
        else:
            text("You try to sneak past the guards, but you trip, giving yourself\naway entirely. The guards attack. Way to go.")
            battle(player,[guardA, guardB])
    else:
        text("You jump out at the guards as they pass, taking them by surprise.\nWell, they weren't THAT surprised, but you'll take what you can get.")
        battle(player,[guardA, guardB])
    
    while True:
        text("The room has three exits, one to the NORTH, one to the EAST,\nand one to the SOUTH. You have no idea where each exit leads.\nWhich path will you take?")
        choice = options(player,["NORTH","EAST","SOUTH"])
        if choice == "NORTH":
            # some room to the north
            text("You walk though the hallway to the north and encounter a small room. There's a door panel in the wall that doesn't seem to open.")
            battleChance = random.random()
            if battleChance < 0.1:
                text("As you're waiting, the door slides open and a giant alien comes out!")
                guardA = enemies.GuardCaptain()
                battle(player,[guardA])
            elif battleChance < 0.5:
                text("As you're waiting, the door slides open and some aliens come out!")
                guardA = enemies.Guard()
                guardB = enemies.Guard()
                battle(player,[guardA, guardB])
            else:
                text("There doesn't seem to be anything here. You decide to head back.")
        elif choice == "EAST":
            pass
            # some other room to the east
        else:
            break
            # the south path is the correct one, the others are dead ends
    
#########################################################################
#                             TITLE SCREEN                              #
#########################################################################
def main():
    print("********************")
    print("This Might Be a Game")
    print(" By Nate (iamvishnu)")
    print("       v0.0.1       ")
    print("********************")
    w(1)
    b(3)
    print("+-+-+-+-+-+-+-+-+-+-+-+")
    print("       MAIN MENU       ")
    print("+-+-+-+-+-+-+-+-+-+-+-+")
    b(1)
    w(0.5)
    global debug
    debug = False
    while True:
        print("Options:")
        print("  - INFO")
        print("  - NEW")
        print("  - LOAD")
        print("  - QUIT")
        if debug:
            print("Debug Options:")
            print("  - TEST BATTLE")
            print("  - CHAPTER SELECT")
        choice = input("Select an option: ").upper()
        if choice == "INFO":
            text("'This Might Be a Game' is an interactive story written in Python\nby Nate(iamvishnu). In this game, you follow along with a story, while\nproviding input to various text prompts. Prompts are case-insensitive.\nType MENU when presented with options to show the menu. Enjoy!")
        elif choice == "NEW":
            while True:
                nameChoice = str(input("What is your name, friend? "))
                if len(nameChoice) > 8:
                    text("That's kind of a mouthful. How about something shorter?")
                elif nameChoice == "":
                    text("Invalid input")
                elif nameChoice.upper() == "FUCK" or nameChoice.upper() == "BITCH":
                    text("What is this, 6th grade? Pick a real name.")
                else:
                    break
            you = actors.Player(nameChoice)
            text("Nice to meet you, " + you.name)
            text("Your story is about to begin.")
            while True:
                ready = input("Are you ready to begin? (Y/N) ").upper()
                if ready == "N":
                    text("You should probably quit now, then. The adventure ahead isn't for babies.")
                elif ready == "Y":
                    text("That's the spirit! Let's get started, shall we?")
                    break
                else:
                    text("Try again, smartass.")
            ChapterOne(you)
        elif choice == "LOAD":
            you = actors.Player("")
            chapter = loadGame(you)
            if chapter == 1:
                ChapterOne(you)
            else:
                text("The save couldn't be loaded properly. Looks like the chapter number wasn't passed back properly.")
        elif choice == "QUIT":
            quit()
        elif choice == "DEBUG":
            debug = not debug
            text("Debug enabled!")
        elif choice == "TEST BATTLE":
            you.name = "TestPlayer"
            guardA = enemies.Guard()
            guardB = enemies.Guard()
            battle(you,[guardA, guardB])
        elif debug and choice == "CHAPTER SELECT":
            while True:
                chapterSelect = options(you,["CHAPTER 1", "BACK"])
                if chapterSelect == "CHAPTER 1":
                    chapterOne()
                elif chapterSelect == "BACK":
                    break
        else:
            text("Invalid input")

if __name__ == "__main__":
    main()