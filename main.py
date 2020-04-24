from aura_setup import SETUP1 as LINKS
from aura_data import RMR
from mana import FlatMana, PrecentMana, MAX_MANA
from util import get_mana_cost
import math

def calculate_local_multiplier(local_link_modifiers):    
    multiplier = 1
    local_rmr = 0
    modifiers = []

    if 'Empower' in local_link_modifiers:
        multiplier *= 1.25

    if 'Enlighten' in local_link_modifiers:
        multiplier *= 1-0.04*(local_link_modifiers['Enlighten']-1)    

    if 'Rmr' in local_link_modifiers:
        local_rmr = local_link_modifiers['Rmr']

    return multiplier, local_rmr

def calculate_aura_mana_cost(rmr):
    total_mana = FlatMana(MAX_MANA)
    for link, aura_dict in LINKS.items():
        multiplier, local_rmr = calculate_local_multiplier(aura_dict['Local'])
        for aura in aura_dict['Auras']:
            total_rmr = max(0, round(1-((rmr + local_rmr)/100.0), 3))
            aura_cost = get_mana_cost(aura.name, aura.level).calculate(multiplier, total_rmr)
            total_mana -= aura_cost
            print(f'{aura.name}: {aura_cost}')

    total_mana.floor()
    return total_mana


def main():
    mana_cost = calculate_aura_mana_cost(RMR)
    print(f'Mana: {mana_cost.mana}/{MAX_MANA}')


if __name__ == "__main__":
    main()

