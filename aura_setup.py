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
        self.supports = []
    
    def support_by(self, support):
        self.supports.append(support)

    def cost(self, rmr):
        multiplier =  reduce(operator.mul, [support.multiplier for support in self.supports], 1)
        return get_mana_cost(self.name, self.level).calculate(multiplier, rmr)

class Link:
    def __init__(self, actives, supports, local_mods):
        self.actives = actives
        self.supports = supports
        self.local_mods = local_mods

        for active in self.actives:
            for support in self.supports:
                if any(tag in support.tags for tag in active.tags):
                    active.support_by(support)
        
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
                print(f'{active.name}: {active.cost(total_rmr)}')
                mana -= active.cost(total_rmr)

        return mana.floor()

            