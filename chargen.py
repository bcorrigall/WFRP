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
    """adds attributes to your character based on race"""
    attribute_dict = {}
    with open('Attributes.txt', 'r') as file:
        race_finder = file.read()
        race_finder = race_finder[race_finder.find(race+' Attributes Start'):race_finder.find(race+' Attributes End')].strip(race+' Attributes Start\n').split('\n')
        for attribute in race_finder:
            attribute = attribute.split('_')
            attribute_dict[attribute[0]] = int(attribute[1])

    for attribute in attribute_dict:
        if attribute not in ['Wounds', 'Fate', 'Resilience', 'Extra Points', 'Movement', 'Experience']:
            #input(f'Roll 2d10 for {attribute}: ')
            roll1 = random.randint(1,10)
            roll2 = random.randint(1,10)
            #print(f'Your first roll for {attribute} was {roll1}. Your Second roll was {roll2}. Your total {attribute} is {roll1+roll2+attribute_dict[attribute]}.')
            attribute_dict[attribute] += roll1
            attribute_dict[attribute] += roll2

    attribute_dict['Experience'] = 120

    if race == 'Halfling':
        attribute_dict['Wounds'] = 2*int(str(attribute_dict['Toughness'])[:1]) + int(str(attribute_dict['Willpower'])[:1])
    else:
        attribute_dict['Wounds'] = int(str(attribute_dict['Strength'])[:1]) + 2*int(str(attribute_dict['Toughness'])[:1]) + int(str(attribute_dict['Willpower'])[:1])

    return attribute_dict

    
def talent_select(race, player_class):
    """adds talents to your character depending on race and class"""
    talent_dict = {}
    with open('Talents.txt', 'r') as file:
        talent_finder = file.read()
        talent_finder = talent_finder[talent_finder.find(race+' Talents Start'):talent_finder.find(race+' Talents End')].strip(race+' Talents Start\n').split('\n')
        for talent in talent_finder:
            talent = talent.split('_')
            talent_dict[talent[0]] = int(talent[1])

    talent_list = []
    talent_chance = []
    with open('Random Talents.txt', 'r') as file:
        for line in file:
                talent_line = line.strip('\n').split('_')
                talent_chance.append(int(talent_line[0]))
                talent_list.append(talent_line[1])
                
    if race == 'Human':
        random_talents = 3
        while random_talents > 0:
            random_talent = random.choices(talent_list, weights = talent_chance)
            print(random_talent)
            if random_talent[0] in talent_dict:
                pass
            elif random_talent[0] not in talent_dict:
                random_talents -= 1
                talent_dict[random_talent[0]] = 1
        del talent_dict['Random']
        savvy_or_suave = random.choice(('Savvy','Suave'))
        if savvy_or_suave == 'Savvy':
            del talent_dict['Suave']
        else:
            del talent_dict['Savvy']

    elif race == 'Dwarf':
        read_or_relentless = random.choice(('Read/Write','Relentless'))
        if read_or_relentless == 'Read/Write':
            del talent_dict['Relentless']
        else:
            del talent_dict['Read/Write']
        resolute_or_strongminded = random.choice(('Resolute','Strong Minded'))
        if resolute_or_strongminded == 'Resolute':
            del talent_dict['Strong Minded']
        else:
            del talent_dict['Resolute']

    elif race == 'Halfling':
        random_talents = 2
        while random_talents > 0:
            random_talent = random.choices(talent_list, weights = talent_chance)
            print(random_talent)
            if random_talent[0] in talent_dict:
                pass
            elif random_talent[0] not in talent_dict:
                random_talents -= 1
                talent_dict[random_talent[0]] = 1
        del talent_dict['Random']

    elif race == 'High Elf':
        coolheaded_or_savvy = random.choice(('Coolheaded','Savvy'))
        if coolheaded_or_savvy == 'Coolheaded':
            del talent_dict['Savvy']
        else:
            del talent_dict['Coolheaded']
        secondsight_or_sixthsense = random.choice(('Second Sight','Sixth Sense'))
        if secondsight_or_sixthsense == 'Second Sight':
            del talent_dict['Sixth Sense']
        else:
            del talent_dict['Second Sight']

    elif race == 'Wood Elf':
        hardy_or_secondsight = random.choice(('Hardy','Second Sight'))
        if hardy_or_secondsight == 'Hardy':
            del talent_dict['Second Sight']
        else:
            del talent_dict['Hardy']
        read_or_veryresilient = random.choice(('Read/Write','Very Resilient'))
        if read_or_veryresilient == 'Very Resilient':
            del talent_dict['Read/Write']
        else:
            del talent_dict['Very Resilient']
    return talent_dict

def race_advances(race):
    """adds advances to your character skills depending on race"""
    base_skill_dict = {}
    skill_list = []
    with open('Skills.txt', 'r') as file:
        skill_finder = file.read()
        skill_finder = skill_finder[skill_finder.find(race+' Skills Start'):skill_finder.find(race+' Skills End')].strip(race+' Skills Start\n').split('\n')
        for skill in skill_finder:
            skill = skill.split('_')
            skill_list.append(skill[0])
            base_skill_dict[skill[0]] = int(skill[1])

    advances = 6
    used_skills = {}
    print(skill_list)
    while advances > 0:
        skill_advance = random.choice(skill_list)
        if advances > 3 and skill_advance not in used_skills:
            print(skill_advance)
            used_skills[skill_advance] = 5
            advances -= 1  
        elif advances > 0 and skill_advance not in used_skills:
            print(skill_advance)
            used_skills[skill_advance] = 3
            advances -= 1  
    return used_skills





def char_sheet(race, player_class, attributes_dict, talents_dict, skills_dict):
    """outputs your character to a text file"""
    with open('Character Sheet.txt', 'w') as file:
        file.write(f'{race} {player_class}\n\nAttributes:\n')
        for attribute in attributes_dict:
            file.write(f'{attribute:<22}  {str(attributes_dict[attribute])}\n')
        file.write('\nTalents:\n')
        for talents in talents_dict:
            file.write(f'{talents:<22}  {str(talents_dict[talents])}\n')
        file.write('\nSkills:\n')
        for skills in skills_dict:
            file.write(f'{skills:<22}  {str(skills_dict[skills])}\n')

def main():
    player_race, race_num = race_select()
    player_class = class_select(player_race)
    attribute_dict = attribute_select(player_race)
    talent_dict = talent_select(player_race,player_class)
    racial_skills = race_advances(race)

    print(racial_skills)
    print(player_race)
    print(player_class)
    print(attribute_dict)

    char_sheet(player_race, player_class, attribute_dict, talent_dict, racial_skills)
    
if __name__ == '__main__': 
    main()