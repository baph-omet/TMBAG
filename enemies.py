from actors import Enemy

class Guard(Enemy):
    def __init__(self):
        Enemy.__init__(self)
        self.health = 3
        self.maxSpecialPoints = 0
        
    name = "Guard"
    desc = "An alien guard. Blueish-gray skin, four deep, black eyes. Carries a spear."
    maxHealth = 3
    expYield = 1
    items = []
    specials = []
    attackChance = 0.8
    defendChance = 0.2
    itemChance = 0
    specialChance = 0
    accuracy = 0.8
    critChance = 0.01
    strength = 1
    defense = 0
    
class GuardCaptain(Enemy):
    def __init__(self):
        Enemy.__init__(self)
        self.health = 5
        self.maxSpecialPoints = 3
        
    name = "Guard Captain"
    desc = "A high-ranking alien guard. Taller and crustier than the foot soldiers."
    maxHealth = 5
    expYield = 3
    items = ["Potion"]
    specials = ["HeavyStrike"]
    attackChance = 0.6
    defendChance = 0.2
    itemChance = 0.1
    specialChance = 0.1
    accuracy = 0.8
    critChance = 0.10
    strength = 2
    defense = 1