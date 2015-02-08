# Base class for special attacks
class Special:
    name = "Dummy"
    desc = "Uninitialized Special Move description"
    damageModifier = 0.0
    numberOfHits = 1
    statUsed = "STRENGTH"
    effect = ""
    effectChance = 0.0
    specialPointCost = 1
    """ name = display name of special attack
        desc = description of special attack
        damageModifier = % damage dealt with respect to base strength or dexterity
        numberOfHits = number of times attack hits
        statUsed = which stat is used to calculate the strength of the attack ("STRENGTH" or "DEXTERITY")
        effect = name of the type of effect
        effectChance = % chance that the special effect will happen
        specialPointCost = # of SP used for this attack
    """
        
# A basic special attack. Inherits most values from base class
class HeavyStrike(Special):
    name = "Heavy Strike"
    desc = "A powerful hit from a melee weapon"
    damageModifier = 2.0

# Same as Heavy Strike, except it uses dexterity instead of strength (good for ranged players)        
class PowerShot(Special):
    name = "Charge Shot"
    desc = "A charged-up shot from a ranged weapon"
    damageModifier = 2.0
    statUsed = "DEXTERITY"