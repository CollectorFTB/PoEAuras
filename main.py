from aura_setup import AuraSetup, Aura, Link
from gem import Empower, Enlighten
from mana import PrecentMana

MAX_MANA = 950
RMR = 86
# class member, TODO: bypass this hack
PrecentMana.MAX_MANA = MAX_MANA

def main():
    # all armour links
    staff = Link(actives=[Aura("Anger"), Aura("Wrath"), Aura("Hatred")], supports=[Empower(4), Enlighten(6)], local_mods={})
    body = Link(actives=[Aura("Malevolence"), Aura("Zealotry"), Aura("Clarity", level=23), Aura("Precision", level=23), Aura("Vitality")], supports=[], local_mods={})
    gloves1 = Link(actives=[Aura("Haste"), Aura("Discipline")], supports=[Empower(4)], local_mods={})
    gloves2 = Link(actives=[Aura("Grace")], supports=[Empower(4)], local_mods={'Rmr': 15})
    boots = Link(actives=[Aura('Determination'), Aura('Dread Banner')], supports=[], local_mods={})
    helmet = Link(actives=[Aura("Purity of Ice"), Aura("Purity of Fire"), Aura("Purity of Lightning"), Aura('Purity of Elements')], supports=[], local_mods={})
    other = Link(actives=[Aura("Aspect of the avian")], supports=[], local_mods={})

    links = [staff, body, gloves1, gloves2, boots, helmet, other]

    setup = AuraSetup(links, rmr=RMR, global_mods={'Spell': 2}, max_mana=MAX_MANA)
    unreserved_mana = setup.print_setup()
    print(f'Mana: {unreserved_mana}/{setup.max_mana}')
    

    
if __name__ == "__main__":
    main()

