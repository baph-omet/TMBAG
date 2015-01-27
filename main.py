#Imports
import time
import random
import methods
import battle
import actors
import enemies
import items

#########################################################################
#                           Game starts here                            #
#########################################################################
# GAME CHAPTERS
## CHAPTER 1
def ChapterOne():
    print("*********")
    print("CHAPTER 1")
    print("*********")
    print("****")
    print("***")
    print("**")
    print("*")
    methods.text("For a while, everything is black. Before too long, you begin to slip back\ninto consciousness. You find yourself sprawled on the cold floor of a sterile,\nwhite room. Bright lights from the ceiling hurt your head as you struggle with\nthe slippery grasp of consciousness.")
    methods.text("You are finally awoken by the feeling of the floor rumbling beneath you.\nyou sit up slowly. There is a door immediately in front of you.")
    while True:
        choice = methods.options(you,["EXAMINE ROOM","TRY DOOR"])
        if choice == "EXAMINE ROOM" and you.money == 0:
            methods.text("The room is square as can be, the floor, walls, and ceiling made up of white panels.\nThere are no windows. The floors seem to be completely bare.")
            methods.text("Actually, it looks like there's something in the corner of the room.\nIt looks like... some money?")
            methods.text("You find $3! Alright.")
            you.money += 3
        elif choice == "EXAMINE ROOM":
            methods.text("There doesn't seem to be anything else here.")
        elif choice == "TRY DOOR":
            methods.text("The door looks heavy and is cold to the touch. There doesn't seem to\nbe a handle, though. No matter what you try, the door doesn't open.")
            break
    methods.text("It's at this time that you hear a pounding on the door. Before you have\ntime to react, the door bursts open. A strange-looking creature strides in.\nIt doesn't look friendly. It's making some weird noise at you and brandishing\na nasty-looking spear. Looks light it's trying to pick a fight.")

    guard = Guard()
    battle(you,[guard])
    
    methods.text("Well that sure was rude.")
    methods.text("That guard that attacked you looked like some kind of alien.\nPerhaps you were abducted? At any rate, it looks\n like they left the door open. You decide not to hang around.")
    methods.text("You find yourself in a long hallway. As you approach the end of\nthe hallway, you notice that the path branches off to the\nleft and right. Which path will you take?")
    
    choice = methods.options(you,["LEFT","RIGHT"])
    if choice == "LEFT":
        pass    
    else:
        pass
    


#########################################################################
#                             TITLE SCREEN                              #
#########################################################################
def main():
    print("********************")
    print("This Might Be a Game")
    print(" By Nate (iamvishnu)")
    print("       v0.0.1       ")
    print("********************")
    methods.w(3)
    methods.b(3)
    print("+-+-+-+-+-+-+-+-+-+-+-+")
    print("       MAIN MENU       ")
    print("+-+-+-+-+-+-+-+-+-+-+-+")
    methods.b(1)
    methods.w(0.5)
    global debug
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
            methods.text("'This Might Be a Game' is an interactive story written in Python\nby Nate(iamvishnu). In this game, you follow along with a story, while\nproviding input to various text prompts. Prompts are case-insensitive.\nType MENU when presented with options to show the menu. Enjoy!")
        elif choice == "NEW":
            while True:
                nameChoice = str(input("What is your name, friend? "))
                if len(nameChoice) > 8:
                    methods.text("That's kind of a mouthful. How about something shorter?")
                else:
                    break
            global you
            you = actors.Player(nameChoice)
            methods.text("Nice to meet you, " + you.name)
            methods.text("Your story is about to begin.")
            i = 0
            while i < 1:
                ready = input("Are you ready to begin? (Y/N) ").upper()
                if ready == "N":
                    methods.text("You should probably quit now, then. The adventure ahead isn't for babies.")
                elif ready == "Y":
                    methods.text("That's the spirit! Let's get started, shall we?")
                    i += 1
                else:
                    methods.text("Try again, smartass.")
            ChapterOne()
        elif choice == "LOAD":
            methods.text("Loading games is not yet implemented. Sorry!")
        elif choice == "EXIT":
            quit()
        elif choice == "DEBUG":
            debug = not debug
            methods.text("Debug enabled!")
        elif choice == "TEST BATTLE":
            you = actors.Player("TestPlayer")
            guardA = enemies.Guard()
            guardB = enemies.Guard()
            battle.battle(you,[guardA, guardB])
        elif debug and choice == "CHAPTER SELECT":
            while True:
                chapterSelect = methods.options(you,["CHAPTER 1", "BACK"])
                if chapterSelect == "CHAPTER 1":
                    chapterOne()
                elif chapterSelect == "BACK":
                    break
        else:
            methods.text("Invalid input")

if __name__ == "__main__":
    main()