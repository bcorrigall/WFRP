import random

def raceselect():
    rnum = random.random()
    if rnum >= 0.99:
        race = 'Wood Elf'
    elif rnum >= 0.98:
        race = 'High Elf'
    elif rnum >= 0.94:
        race = 'Dwarf'
    elif rnum >= 0.9:
        race = 'Halfling'
    elif rnum >= 0: 
        race = 'Human'
    return race

print(raceselect())