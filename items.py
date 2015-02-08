import methods

# Basic classes

class Item():
    name = "Dummy"
    desc = "An uninitialized item"
    buyPrice = 0
    sellPrice = buyPrice / 2
        
class Consumable(Item):
    pass
            
class KeyItem(Item):
    pass
        
class Equipment(Item):
    equipSlot = 0 # 0 = weapon, 1 = head, 2 = armor, 3 = feet
    strengthBonus = 0
    defenseBonus = 0
    dexterityBonus = 0
    critBonus = 0
    accuracyBonus = 0
    attackType = 0 # 0 = melee, 1 = ranged, 2 = no attack
        
######################################################################
# Actual item definitions
######################################################################

## Consumables
class Potion(Consumable):
    name = "POTION"
    desc = "Restores 10HP. Kinda tastes like toothpaste."
    effect = "HEALTH"
    effectStrength = 10
    buyPrice = 5
    sellPrice = 2

## Weapons
class Broom(Equipment):
    name = "BROOM"
    desc = "Amazing. Incredible. A priceless artefact. Treasure it always. +1 Strength"
    equipSlot = 0
    strengthBonus = 1
    
class GuardSpear(Equipment):
    name = "GUARD SPEAR"
    desc = "The same kind of spear that the alien guards carry. Long and sharp, but kind of wobbly. +1 Strength"
    equipSlot = 0
    strengthBonus = 1
    
class GuardPistol(Equipment):
    name = "GUARD PISTOL"
    desc = "A futuristic-looking laser pistol. A ranged weapon, obviously. +1 Dexterity"
    equipSlot = 0
    dexterityBonus = 1
    attackType = 1

## Headgear
class LeatherHelm(Equipment):
    name = "LEATHER HELMET"
    desc = "A soft leather helmet. Doesn't provide much protection on its own.\nTry equipping with other leather armor. +0.5 Defense"
    equipSlot = 1
    defenseBonus = 0.5
    buyPrice = 5
    sellPrice = 2
    
class Bucket(Equipment):
    name = "BUCKET"
    desc = "Just an ordinary bucket. Has a handle that squeaks when turned. +1 Defense"
    equipSlot = 1
    defenseBonus = 1
    buyPrice = 10

## Armor
class LeatherChestplate(Equipment):
    name = "LEATHER CHESTPLATE"
    desc = "A padded leather chestplate. Smells weird, but better than a knife in the gut. +1 Defense"
    equipSlot = 2
    defenseBonus = 1
    name = "LEATHER CHESTPLATE"
    buyPrice = 10
        
## Footgear
class LeatherBoots(Equipment):
    name = "LEATHER BOOTS"
    desc = "Rugged leather boots with long laces. They'll protect you if your toes are stepped on,\nbut that's about it. Try equipping with other leather armor. +0.5 Defense"
    equipSlot = 3
    defenseBonus = 0.5
    buyPrice = 5
    sellPrice = 2
    
    
def allItems():
    itemList = []
    for i in Consumable.__subclasses__():
        itemList.append(i.name)
    return itemList