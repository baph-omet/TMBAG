# Base class for special attacks
class Special:
    def __init__(self):
        self.name = "Dummy"
        self.desc = "Uninitialized Special Move description"
        self.damageModifier = 0.0
        self.numberOfHits = 1
        self.statUsed = "STRENGTH"
        self.effect = ""
        self.effectChance = 0.0
        self.specialPointCost = 1
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
    def __init__(self):
        Special.__init__()
        self.name = "Heavy Strike"
        self.desc = "A powerful hit from a melee weapon"
        self.damageModifier = 2.0

# Same as Heavy Strike, except it uses dexterity instead of strength (good for ranged players)        
class PowerShot(Special):
    def __init__(self):
        Special.__init__()
        self.name = "Charge Shot"
        self.desc = "A charged-up shot from a ranged weapon"
        self.damageModifier = 2.0
        self.statUsed = "DEXTERITY"