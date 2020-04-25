from util import get_mana_cost
from mana import FlatMana

from functools import reduce
import operator

class Aura:
    def __init__(self, name, level=21, quality=23):
        self.name = name
        self.level = level
        self.quality = quality
        self.tags = ['Spell', 'AoE', 'Aura', 'Active']
    
    @property
    def cost(self):
        return get_mana_cost(self.name, self.level)

class Link:
    def __init__(self, actives, supports, local_mods):
        self.actives = actives
        self.supports = supports
        self.local_mods = local_mods

    @property
    def multiplier(self):
        return reduce(operator.mul, [support.multiplier for support in self.supports], 1)

    @property
    def local_rmr(self):
        return self.local_mods['Rmr'] if 'Rmr' in self.local_mods.keys() else 0

class AuraSetup:
    def __init__(self, links, rmr, max_mana, global_mods):
        self.rmr = rmr
        self.links = links
        self.max_mana = max_mana
        self.global_mods = global_mods
    
    def print_setup(self):
        mana = FlatMana(self.max_mana)

        for link in self.links:
            total_rmr = max(0, round(1-(self.rmr + link.local_rmr)/100, 3))
            for active in link.actives:
                print(active.name, active.cost.calculate(link.multiplier, total_rmr))
                mana -= active.cost.calculate(link.multiplier, total_rmr)

        return mana.floor()

            