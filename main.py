from aura_setup import AuraSetup, Aura, Link
from gem import Empower, Enlighten
from mana import PrecentMana

MAX_MANA = 950
RMR = 86

def main():
    # all armour links
    staff = Link(actives=[Aura("Anger"), Aura("Wrath"), Aura("Hatred")], supports=[Empower(4), Enlighten(4)], mana_mods={}, level_mods={'Support':  2})
    body = Link(actives=[Aura("Malevolence"), Aura("Zealotry"), Aura("Clarity"), Aura("Precision"), Aura("Vitality")], supports=[], mana_mods={}, level_mods={})
    gloves1 = Link(actives=[Aura("Haste"), Aura("Discipline")], supports=[Empower(4)], mana_mods={}, level_mods={'Aura': 2, 'AoE': 2, 'Active': 1, 'Support': 1})
    gloves2 = Link(actives=[Aura("Grace")], supports=[Empower(4)], mana_mods={'Rmr': 15}, level_mods={'Aura': 2, 'AoE': 2, 'Active': 1, 'Support': 1})
    boots = Link(actives=[Aura('Determination'), Aura('Dread Banner')], supports=[], mana_mods={}, level_mods={})
    helmet = Link(actives=[Aura("Purity of Ice"), Aura("Purity of Fire"), Aura("Purity of Lightning"), Aura('Purity of Elements')], supports=[], mana_mods={}, level_mods={'Aura': 2})
    other = Link(actives=[Aura("Aspect of the avian")], supports=[], mana_mods={}, level_mods={})

    links = [staff, body, gloves1, gloves2, boots, helmet, other]

    setup = AuraSetup(links, rmr=RMR, level_mods={'Spell': 2}, max_mana=MAX_MANA)
    unreserved_mana = setup.print_setup()
    for link in setup.links: 
        link.print_link()
        
    print(f'Mana: {unreserved_mana}/{setup.max_mana}')
    

    
if __name__ == "__main__":
    main()

