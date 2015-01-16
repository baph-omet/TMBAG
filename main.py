#Imports
import time
import random
from methods import *
from battle import battle
from actors import *
from enemies import *

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
    battle(you,[guard])


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
debug = False
while True:
    print("Options:")
    print("  - INFO")
    print("  - NEW")
    print("  - LOAD")
    print("  - EXIT")
    if debug:
        print("Debug Options:")
        print("  - TEST BATTLE")
        print("  - CHAPTER SELECT")
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
    elif choice == "DEBUG":
        debug = not debug
    elif debug and choice == "TEST BATTLE":
        you = Player("TestPlayer")
        guardA = Guard()
        guardB = Guard()
        battle(you,[guardA, guardB])
    elif debug and choice == "CHAPTER SELECT":
        while True:
            chapterSelect = options("CHAPTER 1", "BACK")
            if chapterSelect == "CHAPTER 1":
                chapterOne()
            elif chapterSelect == "BACK":
                break
    else:
        text("Invalid input")


        
        
