from util import get_mana_cost

class Aura:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.cost = get_mana_cost(self.name, self.level)
