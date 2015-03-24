import random

from methods import text, options
import items
import specials

# Actor definitions
class Actor:
    def __init__(self):
        self.health = 5
        self.guarding = False
        self.strengthMod = 0
        self.defenseMod = 0
        self.accuracyMod = 0
        self.critMod = 0
        self.specialPoints = 3
        
    name = "Dummy"
    desc = ""
    strength = 1
    defense = 0
    maxHealth = 5
    accuracy = 1
    CritChance = 0

    # Attacks a target, target can be any actor (player or enemy)
    def attack(self,target):
        
        # Checks if attack hits or misses
        ## If it misses
        if random.random() > (self.accuracy + self.accuracyMod):
            text(self.name + "'s attack missed!")
            
        ## Else, if it hits
        else:
            # Checks weapon type
            if type(self) == Player and self.equipment[0]:
                # Ranged weapon damage calculation
                if self.equipment[0].attackType == 1:
                    damage = int(self.dexterity + self.dexterityMod) - int(target.defense + target.defenseMod)
                    
                # Non-weapon damage calculation
                elif self.equipment[0].attackType == 2:
                    damage = 0
                    
                # Melee weapon damage calculation
                else:
                    damage = int(self.strength + self.strengthMod) - int(target.defense + target.defenseMod)
            
            # If the executor has no weapon
            else:
                damage = int(self.strength + self.strengthMod) - int(target.defense + target.defenseMod)
            
            # Rolls for a crit
            if random.random() <= (self.critChance + self.critMod):
                text("Critical hit!")
                damage *= 3

            # If damage is less than 0, change it to 0
            if damage <= 0:
                text(self.name + "'s attack failed to damage " + target.name + "!")
                
            # Or, if the damage is positive, attack
            else:
                text(self.name + " attacked " + target.name + " for " + str(damage) + " damage.")
                target.health -= damage
    
    # Uses a special attack. Like a standard attack, but uses a damage modifier based on the attack.
    def specialAttack(self,specialChoice,target):
        # Announces attack
        if type(self) == Player:
            # If it's the player, it picks a random phrase to say
            shoutChoice = random.random()
            if shoutChoice < 0.25:
                text(self.name + ": Take this! " + specialChoice.name + "!")
            elif shoutChoice < 0.5:
                text(self.name + ": Here we go! " + specialChoice.name + "!")
            elif shoutChoice < 0.75:
                text(self.name + ": Die! " + specialChoice.name + "!")
            else:
                text(self.name + ": " + specialChoice.name + "!")
        
        # If the executor isn't a player, they just say a generic phrase
        else:    
            text(self.name + ": " + specialChoice.name + "!")
            
        # If it's the player, and they try to use a ranged special without a ranged item equipped
        if type(self) == Player and specialChoice.statUsed == "DEXTERITY" and self.equipment[0].attackType != 1:
            
            # The attack fails
            text("...but it failed. " + self.name + " forgot that ranged specials aren't possible with a ranged weapon.")
            return
            
        # If the player DOES have a ranged weapon equipped
        elif type(self) == Player and specialChoice.statUsed == "DEXTERITY":
            damage = damage = int((self.dexterity + self.dexterityMod) * specialChoice.damageModifier) - int(target.defense + target.defenseMod)
        
        # Else, if they are an enemy or are using a melee special 
        else:
            damage = damage = int((self.strength + self.strengthMod) * specialChoice.damageModifier) - int(target.defense + target.defenseMod)
            
        # Roll for a crit
        if random.random() <= (self.critChance + self.critMod):
            text("Critical hit!")
            damage *= 3
            
        # If the target's defense is too high
        if damage <= 0:
            text(self.name + "'s attack failed to damage " + target.name + "!")
        
        # Finally, deal damage to the target
        else:
            text(self.name + " attacked " + target.name + " for " + str(damage) + " damage.")
            target.health -= damage
            
        # Decrement user's SP
        self.specialPoints -= specialChoice.specialPointCost
            
    # Enables the user's guard, which raises defense by 1 until next turn
    def defend(self):
        if not self.guarding:
            self.guarding = True
            if self.defense > 0:
                self.defenseMod += self.defense
            else:
                self.defenseMod += 1
            text(self.name + " raised their guard!")
    
    # Disables the user's guard, removing defense buff
    def unDefend(self):
        if self.guarding:
            self.guarding = False
            if self.defense > 0:
                self.defenseMod -= self.defense
            else:
                self.defenseMod -= 1
            text(self.name + " lowered their guard!")
        
    # Activates the effect of an item (usable by all actors)
    def itemEffect(self,itemChoice):
        # Checks if the selected item is a consumable
        for i in items.Consumable.__subclasses__():
            if itemChoice.name == i.name:
                text("Used " + itemChoice.name)
                if itemChoice.effect == "HEALTH":
                    self.health += itemChoice.effectStrength
                    if self.health > self.maxHealth: 
                        self.health = self.maxHealth
                    text(self.name + " recovered " + str(itemChoice.effectStrength) + "HP!")
                else:
                    text("It had no effect!")
                    return
                   
                if type(self) == Player:
                    self.items[itemChoice.name] -= 1
                    if self.items[itemChoice.name] <= 0:
                        self.items[itemChoice.name] = 0
                        if type(self) == Player:
                            text("You used your last " + itemChoice.name)
                        else:
                            text(self.name + " used their last " + itemChoice.name + "!")
                else:
                    self.items.remove(itemChoice)
                return
        
        # If the selected item is equipment, equip it
        else:
            for i in items.Equipment.__subclasses__():
                if itemChoice.name == i.name:
                    break
            else:
                text(self.name + " tried to use a nonexistent item, which obviously did nothing.")
                return
                
            # Make sure the executor is a player
            if self is Enemy:
                print("Enemies can't equip things. Take the equipment out of their inventory.")
                return
            else:
                # Equip the selected item
                self.equip(itemChoice)
                
    # Chooses a special attack
    def chooseSpecial(self):
        # For players...
        specialChoice = None
        if type(self) == Player and not self.specials:
            text("No specials known")
            return
        
        if type(self) == Player:
            # Basically just get a list of the names of all the player's specials, pass them to options(), then get the special attack that corresponds to the choice
            sChoices = []
            for s in self.specials:
                sChoices.append(s.name)
            specialChoiceStr = options(self,sChoices)
            for s in self.specials:
                if specialChoiceStr == s.name.upper():
                    specialChoice = s
            if self.specialPoints < specialChoice.specialPointCost:
                text("You don't have enough SP for this Special.\nYour SP: " + str(self.specialPoints) + "/" + str(self.maxSpecialPoints) + " Required SP for " + specialChoice.name + ": " + str(specialChoice.specialPointCost))
                return
                    
        # For enemies...
        else:
            # If the enemy has no special points or has no specials to use, defend instead
            if self.specialPoints == 0 or not self.specials:
                self.defend()
                return

            # Else randomly pick from their pool of specials, then use it
            else:
                specialChoice = random.choice(self.specials)
                if self.specialPoints < specialChoice.specialPointCost:
                    self.defend()
                    return
        
        # Return whatever was chosen
        return specialChoice
            
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
        self.dexterityMod = 0
        self.accuracy = 0.95
        self.critChance = 0.01
        self.items = {}
        self.specialPoints = 3
        self.specials = []
        self.maxSpecialPoints = 3
        self.equipment = [
            "",
            "",
            "",
            ""
        ]
     
    # Prompts the user to choose an item from their inventory
    def itemChoose(self):
        # Initialize empty list
        itemChoices = []
        itemChoiceObj = None
        
        # Loop over keys in the user's inventory
        for k in self.items:
            # If there's more than one of an item...
            if self.items[k] > 0:
                # ...add it to the list of options
                itemChoices.append(k)
                
        # If any items were added to the list of choices (i.e. the user's inventory is not empty)...
        if itemChoices:
            # Prompt the user for their choice
            target = options(self,itemChoices)
            
            # Check to see if the item is a consumable
            for i in items.Consumable.__subclasses__():
                # If a match was found, create an object whose name matches the chosen item
                if target == i.name:
                    itemChoiceObj = i()
                    # Break to bypass the else clause
                    break
            # If the item is NOT a consumable
            else:
                # Check to see if it's equipment
                for i in items.Equipment.__subclasses__():
                    # If a match is found, create an object of it
                    if target == i.name:
                        itemChoiceObj = i()
                        # Break to bypass else clause
                        break
                # If the item is neither consumable nor equipment, then it must not exist
                else:
                    text("The chosen item doesn't exist")
                    # Quit the function
                    return
            # If an item was verified, return it (as an object)
            return itemChoiceObj
        # If the inventory IS empty, print the following message, then exit
        else:
            text("You don't have any items!")
        
    # Gives the player 1 of a specified item (may update to allow multiples)
    def giveItem(self,item,amount=1):
        if type(amount) != Int or amount < 0:
			text("Invalid amount.")
			return
		# Check to see if the item is a consumable
        for i in items.Consumable.__subclasses__():
            # If a match is found...
            if item.name == i.name:
                # Increases value of the key matching the item by 1, or initializes it to 1 if it doesn't yet exist
                if item.name in self.items:
                    self.items[item.name] += amount
                else:
                    self.items[item.name] = amount
				break
		else: 
			# If the item is NOT a consumable, check to see if it's equipment
			for i in items.Equipment.__subclasses__():
				# See comments in above block
				if item.name == i.name:
					if item.name in self.items:
						self.items[item.name] += amount
					else:
						self.items[item.name] = amount
					text(self.name + " received a " + item.name)
			else:
				return
		if amount != 1:
			text(self.name + " received " + item.name + " x" + str(amount))
		else:
			text(self.name + " received a " + item.name)
        # If the item is neither consumable nor equipment, the function neither returns nor outputs anything

	# Silently removes items from the player's inventory. Only prints stuff if the function is used incorrectly. Use with a itemChoose() method to guarantee that the item is in the player's inventory.
	def removeItem(self,item,amount=1):
		# If the item specified is "all", empty the inventory
		if item.upper == "ALL":
			self.items = {}
		
		# If the user inputs a negative amount
		elif amount < 0:
			text("Attempted to remove a negative number of items from the player. This doesn't make sense. You dun goof'd")
			
		# If the user inputs any other nonsensical value for the amount
		elif type(amount) != Int and amount != "all":
			text("You put a nonsensical amount in this function call. Wuzzamattawichu")
			
		# Otherwise, subtract amount of item from the player
		elif self.items[item.name] > amount:
			self.items[item.name] -= amount
		elif:
			self.items[item.name] = 0
			
			
    
	# Unequips items to the player's inventory. equippedItem is an OBJECT         
    def unequip(self,equippedItem):
        # If the slot for the item is not empty. Basically a failsafe in case somehow an empty slot is passed, which may happen when this method is called in other areas of the code
        if self.equipment[equippedItem.equipSlot] != "":
            # Empty the slot
            self.equipment[equippedItem.equipSlot] = ""
            
            # Add the item back to the player's inventory. If they already have at least one of that item, increase its quantity, else set its quantity to 1.
            if equippedItem.name in self.items:
                self.items[equippedItem.name] += 1
            else:
                self.items[equippedItem.name] = 1
                
            # Remove all stat bonuses from the item
            self.strengthMod -= equippedItem.strengthBonus
            self.dexterityMod -= equippedItem.dexterityBonus
            self.defenseMod -= equippedItem.defenseBonus
            self.accuracyMod -= equippedItem.accuracyBonus
            self.critMod -= equippedItem.critBonus
            text(self.name + " unequpped the" + equippedItem.name)
            
    # Equips items to the player from their inventory. unequippedItem is an OBJECT  
    def equip(self,unequippedItem):
        # If the equip slot for the item is not empty
        if self.equipment[unequippedItem.equipSlot] != "":
            # Unequip the item in that slot
            self.unequip(self.equipment[unequippedItem.equipSlot])
            
        # Add the item to its respective slot
        self.equipment[unequippedItem.equipSlot] = unequippedItem
        
        # Add stat bonuses to the player's stat modifiers
        self.strengthMod += unequippedItem.strengthBonus
        self.dexterityMod += unequippedItem.dexterityBonus
        self.defenseMod += unequippedItem.defenseBonus
        self.accuracyMod += unequippedItem.accuracyBonus
        self.critMod += unequippedItem.critBonus
        
        # Remove the item from the player's regular inventory
        self.items[unequippedItem.name] -= 1
        text(self.name + " equipped a " + unequippedItem.name)
              
    # Throws away an item. tossItem should be an OBJECT
    def toss(self,tossItem):
        # Double-check to make sure the item is actually in the player's inventory
        for e in self.items:
            if tossItem.name == e:
                break
            
        else:
            text("That item couldn't be found. Check the source code.")
            return
        for e in KeyItem.__subclasses__():
            if tossItem.name == e:
                print(tossItem.name,"is a key item. You'd be stupid to throw this away.")
                return
        else:
            # Chuck that shit
            self.items[tossItem] -= 1
            text(self.name + " threw away 1 " + tossItem.name)
        
    # Silently remove an item from the player's inventory. Should be for internal use only.
	def removeItem(self,item,amount=1):
		if self.items[item.name]:
			if amount == "all":
				self.items[item.name] = 0
			else:
				self.items[item.name] -= amount
	
	# Examine an enemy during battle. target is passed by the battle engine, and is an OBJECT
    def examine(self,target):
        # Print the target's stats
        # FUTURE NOTE: May add a check to make sure that the target is an enemy, to prevent crashes, even though this is probably redundant by this point.
        text("You take a closer look at " + target.name)
        print("=" * 15)
        print("|",target.name)
        print("| HP: " + str(target.health) + "/" + str(target.maxHealth))
        print("| Strength:",target.strength)
        print("| Defense:",target.defense)
        print("| Accuracy:",str(int(target.accuracy * 100)) + "%")
        print("| Critical Chance:",str(int(target.critChance * 100)) + "%")
        print("|",target.desc)
        text("=" * 15)
    
    # Allows the player to run away from a battle. enemies is a LIST of enemies (the same one passed to the battle engine), escape is a BOOL (the same one passed to the battle engine, defaults True)
    # FUTURE NOTE: Change run calculation. Currently too favorable to players
    def runAway(self, enemies, escape):
        # Checks to make sure the player can escape
        if escape:
            avgSkill = 0
            # Loop over enemies
            for i in enemies:
                # For each enemy, their "skill" is the sum of their % accuracy and % crit chance
                avgSkill += (i.accuracy + i.critChance)
                
            # Averages the skill stat
            avgSkill = avgSkill / len(enemies)
            
            # The chance that the player will escape is the ratio of their skill to the enemy skill multiplied by the ratio of their max health to their current health. Meaning the more "skilled" the enemies, the harder it is to escape, while the more injured the player is, the easier it is to escape.
            runChance = ((self.accuracy + self.critChance) / avgSkill) * (self.maxHealth / self.health)
            
            # Rolls for escape
            if random.random() <= runChance:
                text("You successfully escaped from the battle!")
                # Returns a successful escape
                return True
            else:
                text("You couldn't escape!")
                # Returns an unsuccessful escape
                return False
        # If the player is unable to escape from this battle at all (i.e. escape is False)
        else:
            text("You cannot escape from this battle!")
            return False
        
    # Increases the player's level
    # FUTURE NOTE: Does not verify required EXP, may change this in the future, even though it's redundant
    def levelUp(self):
        # Excess exp rolls over to the next level
        self.exp = self.exp - self.expNextLevel
        
        # Level is incremented
        # Initial: 1
        self.level += 1
        text("You leveled up!")
        text("You reached Level " + str(self.level) + "!")
        print("=" * 15)
        
        # Next level's exp requirement is twice that of the previous level
        # Initial: 5
        # expNextLevel = 5 * 2 ** (level - 1)
        self.expNextLevel *= 2
        
        # Crit chance is increased by a percetage equal to the new level
        # Initial: 0.01 (1%)
        # critChance = 0.01 + (math.sum(range(level)) - 1) * 0.01
        self.critChance += self.level * 0.01
        print("Crit Chance + " + str(self.level) + "%")
        
        # Max health is increased by an amount equal to the new level
        # Initial: 10
        # maxHealth = 10 + math.sum(range(2,level)) * 0.01
        self.maxHealth += self.level
        print("Max Health +", self.level)
        
        # Increase SP by 1, then refill SP
        # Initial: 3
        # maxSpecialPoints = 3 + level - 1
        self.maxSpecialPoints += 1
        self.specialPoints = self.maxSpecialPoints
        print("SP + 1")
        
        # Defense is increased by 1 on odd numbered levels
        # Initial: 0
        # defense = level // 2
        if self.level % 2 == 1:
            self.defense += 1
            print("Defense + 1")
        
        # Health is refilled (I love it when games do this)
        self.health = self.maxHealth
        print("=" * 15)
        
        # Player picks to either increase strength or dexterity by one. Lets the player choose their development path a bit.
        text("Choose a level-up bonus!")
        levelUpBonus = options(self,["STRENGTH","DEXTERITY"])
        if levelUpBonus == "STRENGTH":
            self.strength += 1
            print("Strength + 1")
        else:
            self.dexterity += 1
            print("Dexterity + 1")
            
        # At lv2, the player either learns Heavy Strike special or Power Shot special, depending on their stats
        if self.level == 2:
            if self.strength > self.dexterity:
                self.learnSpecial(specials.HeavyStrike)
            elif self.strength < self.dexterity:
                self.learnSpecial(specials.PowerShot)
    
    # Debug function that sets a player to a level and sets their base stats. Assumes strength upgrades were chosen on every level instead of dexerity
    def setLevel(self,newLevel):
        self.expNextLevel = 5 * 2 ** (newLevel - 1)
        self.critChance = 0.01 + int(sum(range(2,newLevel))) * 0.01
        self.maxSpecialPoints = 2 + newLevel
        self.maxHealth = 10 + sum(range(2,newLevel))
        self.health = self.maxHealth
        self.defense = (newLevel - 1) // 2
        self.strength = newLevel
        self.specials = [specials.HeavyStrike]
    
    # Adds a special move to the player's repertoire
    def learnSpecial(self,newSpecial):
        # Checks to see if the player already knows the move to avoid duplicates
        for s in self.specials:
            if newSpecial.name == s.name:
                print(self.name + " already knows " + s.name + "!")
                return
        
        # If the move is not already known
        self.specials.append(newSpecial)
        text(self.name + " learned the special attack " + newSpecial.name)
    
    # Renames the player     
    def rename(self):
        text("It's at this point in your adventure that you decide to forge a new itentity for yourself. You're the boss. Who's to tell you what your name is?")
        self.name = input("What shall your new name be? ")
        text("You are now known as " + self.name + ", a name certainly 100, nay, 1000 times the superior of your old moniker.")

        
    
# Enemy definitions
class Enemy(Actor):
    def __init__(self):
        Actor.__init__(self)
    
    attackChance = 1
    defendChance = 0
    itemChance = 0
    specialChance = 0
    expYield = 1
    moneyYield = 1
        
    # Enemy item use behavior
    def itemUse(self):
        # If the user has no items, defend instead
        if not self.items:
            self.defend()
        
        # If they do, randomly pick from their list of items, then use it on themselves
        else:
            itemChoice = random.choice(self.items)
            self.itemEffect(itemChoice)
            
    
    # How enemies choose what to do (spoiler: it's random)
    def behavior(self,target):
        # The value for their action is a random float from 0 to 1
        action = random.random()
        
        # The next few blocks use this random number to choose the enemy's attack based on its inherent behavior
        if action <= self.attackChance:
            self.attack(target)
        elif action <= (self.attackChance + self.defendChance) and action > self.attackChance:
            self.defend()
        elif action <= (self.attackChance + self.defendChance + self.itemChance) and action > (self.attackChance + self.defendChance):
            self.itemUse()
            text
        elif action <= (self.attackChance + self.defendChance + self.itemChance + self.specialChance) and action > (self.attackChance + self.defendChance + self.itemChance):
            specialChoice = self.chooseSpecial()
            if specialChoice:
                self.specialAttack(specialChoice, target)

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
