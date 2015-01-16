from actors import Enemy

class Guard(Enemy):
    def __init__(self):
        Enemy.__init__(self)
        self.name = "Guard"
        self.sesc = "An alien guard. Blueish-gray skin, four deep, black eyes.\
     Carries a spear."
        self.strength = 1
        self.defense = 0
        self.health = 3
        self.maxHealth = 3
        self.expYield = 1
        self.items = []
        self.specials = []
        self.attackChance = 0.8
        self.defendChance = 0.2
        self.itemChance = 0
        self.specialChance = 0
        self.accuracy = 0.8
        self.critChance = 0.01
