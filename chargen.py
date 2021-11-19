import random

def race_select():
    """returns a randomly selected race"""
    race_num = random.randint(1,100)
    if race_num == 100:
        race = 'Wood Elf'
    elif race_num == 99:
        race = 'High Elf'
    elif race_num >= 95:
        race = 'Dwarf'
    elif race_num >= 91:
        race = 'Halfling'
    elif race_num <= 90: 
        race = 'Human'
    return race, race_num

race, racenum = race_select()

def class_select(race):
    """returns a randomly selected class depending on race"""
    class_list = []
    class_chance = []
    with open(race+' Classes.txt', 'r') as file:
        for line in file:
            class_line = line.strip('\n').split('_')
            class_chance.append(int(class_line[0]))
            class_list.append(class_line[1])
    player_class = random.choices(class_list, weights = class_chance)
    return player_class[0]

print(class_select('Wood Elf'))