import random

def raceselect():
    """returns a randomly selected race"""
    rnum = random.randint(1,100)
    if rnum == 100:
        race = 'Wood Elf'
    elif rnum == 99:
        race = 'High Elf'
    elif rnum >= 95:
        race = 'Dwarf'
    elif rnum >= 91:
        race = 'Halfling'
    elif rnum <= 90: 
        race = 'Human'
    print(rnum)
    return race

def class_select():
    """"""



print(raceselect())