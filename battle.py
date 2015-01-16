from methods import *
from actors import *
from enemies import *

#Battle Engine
def battle(hero,enemies,run=True):
    #enemies is a [list] of enemy objects, not strings
    #run is a boolean, set to false if player cannot escape battle (bosses, etc.)
    battleExp = 0
    battleMoney = 0
    turn = 0
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
        print("|" + " " * int((10 - len(hero.name))/2) + hero.name + " " * \
              int((10 - len(hero.name))/2) + "|")
        print("| HP: " + str(hero.health) + "/" + str(hero.maxHealth))
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
            print("| " + i.name + " " + enemyNumber)
            print("| HP: " + str(i.health) + "/" + str(i.maxHealth))
            if i.guarding:
                print("| Defending!")
            print("*" * 12)

            hero.unDefend()

        #Choose a battle command
        while True:
            battleChoice = options("ATTACK","SPECIAL","DEFEND","ITEM","MENU",\
                                   "RUN")
            if battleChoice == "ATTACK":
                #select a target
                if len(enemies) > 1:
                    while True:
                        print("Pick a Target:")
                        n = 1
                        for i in enemies:
                            print("  ",str(n) + ":",i.name,n)
                            n += 1
                        target = eval(input("Which enemy will you attack? ")) - 1
                        if target in range(len(enemies)):
                            target = enemies[target]
                            break
                        else:
                            text("Incorrect target")
                else:
                    target = enemies[0]
                hero.attack(target)
                break
            elif battleChoice == "SPECIAL":
                pass
            elif battleChoice == "DEFEND":
                hero.defend()
                break
            elif battleChoice == "ITEM":
                pass
            elif battleChoice == "RUN":
                pass
            
        # checks for dead enemies
        for i in enemies:
            if i.health <= 0:
                text(i.name + " was defeated!")
                # EXP is gained in-battle a-la Pokemon, allowing a player to be healed if they level up mid-battle.
                text("You gained " + str(i.expYield) + " Experience")
                hero.exp += i.expYield
                battleExp +=
                if hero.exp >= hero.expNextLevel:
                    hero.levelUp()
                battleMoney += i.moneyYield
                enemies.remove(i)
                
        # checks for victory
        if not enemies:
            print("!" * 11)
            print("! VICTORY !")
            print("!" * 11)
            print("Total EXP Gained:",battleExp)
            print("Money Collected: $" + str(battleMoney)
            print("Current Health:",str(hero.health) + "/" + str(hero.maxHealth))
            print("=" * 10)
            print("=" * 9)
            print("=" * 8)
            print("=" * 7)
            print("=" * 6)
            print("=" * 5)
            print("=" * 4)
            print("=" * 3)
            break

        # enemy attacks
        for i in enemies:
            print(i.name,str(enemies.index(i) + 1) + ":")
            i.unDefend()
            i.behavior(hero)
            
        # checks for dead player
        if hero.health <= 0:
            text(i.name + " was defeated!")
            text("X X X GAME OVER X X X")
            quit()
