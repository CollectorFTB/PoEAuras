import math

MAX_MANA = 1086

def calculate_round_mana(mana, multiplier, rmr):
    return math.ceil(round(mana * multiplier * rmr, 3))

class Mana:
    def calculate(self, multiplier, rmr):
        return self.__class__(calculate_round_mana(self.mana, multiplier, rmr))


class PrecentMana(Mana):
    def __init__(self, mana):
        self.mana = mana
    
    @property
    def cost(self):
        return MAX_MANA * self.mana/100.0

    def __repr__(self):
        return str(self.mana) + '%'

class FlatMana(Mana):
    def __init__(self, mana):
        self.mana = mana
        self.cost = mana

    def __sub__(self, other):
        try:
            return FlatMana(self.cost - other.cost)
        except:
            return NotImplemented

    def __repr__(self):
        return str(self.mana)

    def floor(self):
        self.mana = math.floor(self.mana)
        return self