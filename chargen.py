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

def attribute_select(race):
    attribute_dict = {}
    with open('Attributes.txt', 'r') as file:
        race_finder = file.read()
        race_finder = race_finder[race_finder.find(race+' Attributes Start'):race_finder.find(race+' Attributes End')].strip(race+' Attributes Start\n').split('\n')
        for attribute in race_finder:
            attribute = attribute.split('_')
            attribute_dict[attribute[0]] = int(attribute[1])

    for attribute in attribute_dict:
        if attribute not in ['Wounds', 'Fate', 'Resilience', 'Extra Points', 'Movement', 'Experience']:
            roll1 = random.randint(1,10)
            attribute_dict[attribute] += roll1

            roll2 = random.randint(1,10)
            attribute_dict[attribute] += roll2

    attribute_dict['Experience'] = 120

    if race == 'Halfling':
        attribute_dict['Wounds'] = 2*int(str(attribute_dict['Toughness'])[:1]) + int(str(attribute_dict['Willpower'])[:1])
    else:
        attribute_dict['Wounds'] = int(str(attribute_dict['Strength'])[:1]) + 2*int(str(attribute_dict['Toughness'])[:1]) + int(str(attribute_dict['Willpower'])[:1])



    print(attribute_dict)


print(class_select('Dwarf'))
attribute_select('Dwarf')