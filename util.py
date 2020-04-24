from aura_data import FLAT_COSTS, PRECENT_COSTS
from mana import FlatMana, PrecentMana

def get_mana_cost(name, level):
    if name in FLAT_COSTS.keys():
        mana_cost = FLAT_COSTS[name][level-1] # levels are 1 indexed
        return FlatMana(mana_cost)
    elif name in PRECENT_COSTS.keys():
        mana_cost = PRECENT_COSTS[name]
        return PrecentMana(mana_cost)
