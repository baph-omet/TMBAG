import random
from methods import *

#Actor definitions
class Actor:
    def __init__(self):
        self.name = "Dummy"
        self.desc = ""
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
        self.guarding = False

    def attack(self,target):
        if random.random() > self.accuracy:
            text(self.name + "'s attack missed!")
        else:
            if random.random() <= self.critChance:
                text("Critical hit!")
                damage = self.strength * 3 - target.defense
            else:
                damage = self.strength - target.defense
            text(self.name + " attacked " + target.name + " for " + str(damage)\
                 + " damage.")
            target.health -= damage
        # attacks a target. target can be any actor (player or enemy)

    def defend(self):
        if not self.guarding:
            self.guarding = True
            self.defense += 1
            text(self.name + " raised their guard!")

    def item(self, item, target):
        pass
    
##Player definition
class Player(Actor):
    def __init__(self,playerName):
        self.name = playerName
        self.money = 0
        self.level = 1
        self.exp = 0
        self.expNextLevel = 5
        self.health = 10
        self.maxHealth = 10
        self.strength = 1
        self.defense = 0
        self.dexterity = 1
        self.accuracy = 0.95
        self.critChance = 0.01
        
    def levelUp(self):
        self.exp = self.exp - self.expNextLevel
        self.level += 1
        text("You leveled up!")
        text("You reached Level",self.level)
        print("=" * 15)
        self.expNextLevel *= 2
        self.critChance += self.level * 0.01
        print("Crit Chance +", str(self.level) + "%")
        self.maxHealth += self.level
        print("Crit Chance +", self.level)
        self.defense += 1
        print("Defense + 1")
        self.health = self.maxHealth
        print("=" * 15)
        text("Choose a level-up bonus!")
        levelUpBonus = options("STRENGTH","DEXTERITY")
        if levelUpBonus == "STRENGTH":
            self.strength += 1
            print("Strength + 1")
        else:
            self.dexterity += 1
            print("Dexterity + 1")
        ''' raises the player to their next level
            any leftover exp is kept
            expNextLevel is doubled
            critChance is increased by a percentage equal to the new level
            maxHealth is increased by an amount equal to the new level
            defense is increased by 1
            either strength or dexterity is increased by 1
            health is refilled (i always love it when games do that)'''
            
    def rename(self):
        text("It's at this point in your adventure that you decide to forge a new\
     itentity for yourself. You're the boss. Who's to tell you what your name is?")
        self.name = input("What shall your new name be? ")
        text("You are now known as " + self.name + ", a name certainly 100, nay, 1000 times\
     the superior of your old monicker.")
        # renames the player

##Enemy definitions
class Enemy(Actor):
    def item(self):
        print("Enemy item use not yet implemented")
    def special(self):
        print("Enemy special attacks not yet implemented")
        
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
