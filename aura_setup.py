from util import get_mana_cost
from mana import FlatMana, Mana

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
        support.apply_to(self)
        self.supports.append(support)

    def cost(self, rmr):
        multiplier =  reduce(operator.mul, [support.multiplier for support in self.supports], 1)
        return get_mana_cost(self.name, self.level).calculate(multiplier, rmr)

class Link:
    def __init__(self, actives, supports, mana_mods, level_mods):
        self.actives = actives
        self.supports = supports
        self.mana_mods = mana_mods
        self.level_mods = level_mods

        self.apply_level_mods(self.level_mods)

        for active in self.actives:
            for support in self.supports:
                if any(tag in support.support_list for tag in active.tags):
                    active.support_by(support)
        

    @property
    def local_rmr(self):
        return self.mana_mods['Rmr'] if 'Rmr' in self.mana_mods.keys() else 0

    def apply_level_mods(self, level_mods):
        for tag, bonus in level_mods.items():
            for active in self.actives:
                if tag in active.tags:
                    active.level += bonus

            for support in self.supports:
                if tag in support.tags:
                    support.level += bonus

    def print_link(self):
        for active in self.actives:
            print(f'{active.name}({active.level}/{active.quality})')
        for support in self.supports:
            print(f'{support.name}({support.level}/{support.quality})')


class AuraSetup:
    def __init__(self, links, rmr, max_mana, level_mods):
        self.rmr = rmr
        self.links = links
        self.max_mana = max_mana
        self.level_mods = level_mods

        for link in self.links:
            link.apply_level_mods(self.level_mods)

        Mana.MAX_MANA = self.max_mana
    
    def print_setup(self):
        mana = FlatMana(self.max_mana)

        for link in self.links:
            total_rmr = max(0, round(1-(self.rmr + link.local_rmr)/100, 3))
            for active in link.actives:
                print(f'{active.name}: {active.cost(total_rmr)}')
                mana -= active.cost(total_rmr)

        return mana.floor()

            