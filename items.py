import methods

# Basic classes

class Item():
    def __init__(self):
        self.name = "Dummy"
        self.desc = "An uninitialized item"
        self.buyPrice = 0
        self.sellPrice = 0
        
class Consumable(Item):
    def __init__(self):
        Item.__init__(self)
            
class KeyItem(Item):
    def __init__(self):
        Item.__init__(self)
        
class Equipment(Item):
    def __init__(self):
        Item.__init__(self)
        self.equipSlot = 0 # 0 = weapon, 1 = head, 2 = armor, 3 = feet
        self.strengthBonus = 0
        self.defenseBonus = 0
        self.dexterityBonus = 0
        self.critBonus = 0
        self.accuracyBonus = 0
        self.attackType = 0 # 0 = melee, 1 = ranged, 2 = no attack
        
######################################################################
# Actual item definitions
######################################################################

## Consumables
class Potion(Consumable):
    def __init__(self):
        Consumable.__init__(self)
        self.name = "POTION"
        self.desc = "Restores 10HP. Kinda tastes like toothpaste."
        self.effect = "HEALTH"
        self.effectStrength = 10
        self.buyPrice = 5
        self.sellPrice = 2
        
    name = "POTION"
## Weapons
        
## Headgear
class LeatherHelm(Equipment):
    def __init__(self):
        Equipment.__init__(self)
        self.name = "LEATHER HELMET"
        self.desc = "A soft leather helmet. Doesn't provide much protection on its own.\nTry equipping with other leather armor."
        self.equipSlot = 1
        self.defenseBonus = 0.5
    name = "LEATHER HELMET"

## Armor
class LeatherChestplate(Equipment):
    def __init__(self):
        Equipment.__init__(self)
        self.name = "LEATHER CHESTPLATE"
        self.desc = "A padded leather chestplate. Smells weird, but better than a knife in the gut."
        self.equipSlot = 2
        self.defenseBonus = 1
    name = "LEATHER CHESTPLATE"
        
## Footgear
class LeatherBoots(Equipment):
    def __init__(self):
        Equipment.__init__(self)
        self.name = "LEATHER BOOTS"
        self.desc = "Rugged leather boots with long laces. They'll protect you if your toes are stepped on,\nbut that's about it. Try equipping with other leather armor."
        self.equipSlot = 3
        self.defenseBonus = 0.5
    name = "LEATHER BOOTS"
    
def allItems():
    itemList = []
    for i in Consumable.__subclasses__():
        itemList.append(i.name)
    return itemList