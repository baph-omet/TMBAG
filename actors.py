import random
from methods import *
from items import *

# Actor definitions
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
        self.accuracy = 1
        self.CritChance = 0
        self.guarding = False
        self.strengthMod = 0
        self.defenseMod = 0
        self.accuracyMod = 0
        self.critMod = 0
        self.moneyYield = 1

    def attack(self,target):
        if random.random() > (self.accuracy + self.accuracyMod):
            text(self.name + "'s attack missed!")
        else:
            if random.random() <= (self.critChance + self.critMod):
                text("Critical hit!")
                damage = (self.strength + self.strengthMod) * 3 - (target.defense + target.defenseMod)
            else:
                damage = (self.strength + self.strengthMod) - (target.defense + target.defenseMod)
            if damage <= 0:
                text(self.name + "'s attack failed to damage " + target.name + "!")
            else:
                text(self.name + " attacked " + target.name + " for " + str(damage) + " damage.")
                target.health -= damage
        # attacks a target. target can be any actor (player or enemy)

    def defend(self):
        if not self.guarding:
            self.guarding = True
            self.defenseMod += 1
            text(self.name + " raised their guard!")
    def unDefend(self):
        if self.guarding:
            self.guarding = False
            self.defenseMod -= 1
            text(self.name + " lowered their guard!")

    def item(self, item, target):
        pass
    
# Player definition
class Player(Actor):
    def __init__(self,playerName):
        Actor.__init__(self)
        self.name = playerName
        self.money = 0
        self.level = 1
        self.exp = 0
        self.expNextLevel = 5
        self.health = 10
        self.maxHealth = 10
        self.dexterity = 1
        self.accuracy = 0.95
        self.critChance = 0.01
        self.items = {x:0 for x in Consumable.__subclasses__()}
        self.unequipped = {x:0 for x in Equipment.__subclasses__()}
        self.equipment = [
            "",
            "",
            "",
            ""
        ]
        
    def examine(self,target):
        text("You take a closer look at " + target.name)
        print("=" * 15)
        print("|",target.name)
        print("| HP: " + str(target.health) + "/" + str(target.maxHealth))
        print("| Strength:",target.strength)
        print("| Defense:",target.defense)
        print("| Accuracy:",str(int(target.accuracy * 100)) + "%")
        print("| Critical Chance:",str(int(target.critChance * 100)) + "%")
        print("|",target.desc)
        print("=" * 15)
    
    def runAway(self, enemies, escape):
        if escape:
            avgSkill = 0
            n = 0
            for i in enemies:
                avgSkill += (i.accuracy + i.critChance)
                n += 1
            avgSkill = avgSkill / n
            runChance = ((self.accuracy + self.critChance) / avgSkill) * (self.maxHealth / self.health)
            if random.random() <= runChance:
                text("You successfully escaped from the battle!")
                return True
            else:
                text("You couldn't escape!")
                return False
        else:
            text("You cannot escape from this battle!")
            return False
        
    def levelUp(self):
        # Excess exp rolls over to the next level
        self.exp = self.exp - self.expNextLevel
        
        # Level is incremented
        self.level += 1
        text("You leveled up!")
        text("You reached Level",str(self.level) + "!")
        print("=" * 15)
        
        # Next level's exp requirement is twice that of the previous level
        self.expNextLevel *= 2
        
        # Crit chance is increased by a percetage equal to the new level
        self.critChance += self.level * 0.01
        print("Crit Chance +", str(self.level) + "%")
        
        # Max health is increased by an amount equal to the new level
        self.maxHealth += self.level
        print("Max Health +", self.level)
        
        # Defense is increased by 1
        self.defense += 1
        print("Defense + 1")
        
        # Health is refilled (I love it when games do this)
        # In the future when I finally implement specials and SP, possibly refill SP
        self.health = self.maxHealth
        print("=" * 15)
        
        # Player picks to either increase strength or dexterity by one. Lets the player choose their development path a bit.
        text("Choose a level-up bonus!")
        levelUpBonus = options(self,"STRENGTH","DEXTERITY")
        if levelUpBonus == "STRENGTH":
            self.strength += 1
            print("Strength + 1")
        else:
            self.dexterity += 1
            print("Dexterity + 1")
    
    # Renames the player     
    def rename(self):
        text("It's at this point in your adventure that you decide to forge a new\
     itentity for yourself. You're the boss. Who's to tell you what your name is?")
        self.name = input("What shall your new name be? ")
        text("You are now known as " + self.name + ", a name certainly 100, nay, 1000 times\
     the superior of your old monicker.")

# Enemy definitions
class Enemy(Actor):
    def __init__(self):
        Actor.__init__(self)
        self.attackChance = 1
        self.defendChance = 0
        self.itemChance = 0
        self.specialChance = 0
    def item(self):
        text(self.name + " tried to use an item, but items are not yet implemented!")
    def special(self):
        text(self.name + " tried to use a special attack, but special attacks are not yet implemented!")
        
    def behavior(self,target):
        action = random.random()
        if action <= self.attackChance:
            self.attack(target)
        elif action <= (self.attackChance + self.defendChance) and action > self.attackChance:
            self.defend()
        elif action <= (self.attackChance + self.defendChance + self.itemChance) and action > (self.attackChance + self.defendChance):
            self.item()
        elif action <= (self.attackChance + self.defendChance + self.itemChance + self.specialChance) and action > (self.attackChance + self.defendChance + self.itemChance):
            self.special()
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
