import pprint
import random
import os
import json
from dataclasses import dataclass
from operator import attrgetter
import csv

SCRIPT_DIR = os.path.dirname(__file__)
FILE_FACTIONS = os.path.join(SCRIPT_DIR, 'static', 'factions.json')
FILE_FACTION_AFILIATIONS = os.path.join(SCRIPT_DIR, 'static', 'faction_afiliations.json')
FILE_POSITIONS = os.path.join(SCRIPT_DIR, 'static', 'positions.json')
FILE_CITIZEN_RELATIONS = os.path.join(SCRIPT_DIR, 'static', 'citizen_relations.json')
FILE_NAMES_MALE = os.path.join(SCRIPT_DIR, 'static', 'names_male.txt')
FILE_NAMES_FEMALE = os.path.join(SCRIPT_DIR, 'static', 'names_female.txt')
FILE_NAMES_INTERESTING = os.path.join(SCRIPT_DIR, 'static', 'names_interesting.txt')

def generate_random_city():
    city_generator_inputs = gather_default_input_values()
    city_generator_manual_values = gather_manual_input_values()
    city_generator_conditions = gather_input_conditions()

    factions = create_factions_list(
        city_generator_inputs['number_of_factions'],
        city_generator_conditions['MANUAL_FACTION_CHOICE'],
        city_generator_manual_values['factions']
    )

    sexes = create_sexes_list(
        city_generator_inputs['favor_females'],
        city_generator_inputs['favor_males'])

    citizens = []
    # Generate citizens
    for citizen in range(city_generator_inputs['number_of_vampires']):
       citizens.append(generate_citizen(
            city_generator_inputs,
            factions,
            sexes))

    # Generate citizen relations
    citizens = create_citizen_relations(citizens, city_generator_inputs['minimum_sireing_gap'])

    return citizens

def gather_default_input_values():
    inputs = {
        'number_of_vampires': 20,
        'number_of_factions': 3,
        'age_average': 150,
        'age_standard_deviation': 120,
        'favor_females': 70,
        'favor_males': 30,
        'minimum_sireing_gap': 20
    }
    return inputs

def gather_manual_input_values():
    manual_input_values = {
        'factions': ['Camarilla']
    }

    return manual_input_values

def gather_input_conditions():
    condtitions = {
        'MANUAL_FACTION_CHOICE': False
    }
    return condtitions

def create_factions_list(number_of_factions, faction_choice_condition, manual_factions_list):
    if faction_choice_condition == False:
        with open(FILE_FACTIONS) as json_file:
            factions = json.load(json_file)
            factions_list = random.sample(factions, number_of_factions)
    else:
        factions_list = manual_factions_list

    return factions_list

def create_sexes_list(n_male, n_female):
    sexes_list = ['Male' for i in range(1, n_male)]
    female_list = ['Female' for i in range(1, n_female)]
    sexes_list.extend(female_list)

    return sexes_list

@dataclass
class citizen:
    name: str
    faction: str
    position: str 
    age: int
    sex: str
    clan: str
    sire: str
    generation: int
    children: list
    superior: dict
    relations: dict

def generate_citizen(inputs, factions, sexes):
    generated_age = abs(int(random.normalvariate(inputs['age_average'], inputs['age_standard_deviation'])))
    generated_sex = random.choice(sexes)
    generated_name = create_name(generated_sex)
    generated_faction = random.choice(factions)
    generated_clan = create_clans_list(generated_faction)[0]

    generted_citizen = citizen(
        faction = generated_faction,
        position = None,
        age = generated_age,
        name = generated_name,
        sex =  generated_sex,
        clan = generated_clan,
        sire =  None,
        generation =  None,
        children = [],
        superior = None,
        relations = None
    )
    
    return generted_citizen

def create_name(sex):
    male_names = []
    female_names = []
    surnames = []
    female_names = convert_txt_to_string_list(FILE_NAMES_FEMALE, female_names)
    male_names = convert_txt_to_string_list(FILE_NAMES_MALE, male_names)
    surnames = convert_txt_to_string_list(FILE_NAMES_INTERESTING, surnames)

    name_surname = random.choice(surnames)

    if sex == 'Female':
        name_christian = random.choice(female_names)
    else:
        name_christian = random.choice(male_names)

    name_full = name_christian + ', ' + name_surname

    return name_full

def convert_txt_to_string_list(filename, listname):
    with open(filename) as inf:
        listname = inf.readlines()
        listname = [name.strip() for name in listname]
    return listname
    
def create_clans_list(faction):
    with open(FILE_FACTION_AFILIATIONS) as json_file:
        clans = json.load(json_file)
        clans_list = random.sample(clans[faction], 1)
    return clans_list

def create_citizen_relations(citizens, minimum_sireing_gap):
    with open(FILE_POSITIONS) as json_file:
        positions = json.load(json_file)    

    citizens = give_positions(positions, citizens)
    citizens = relate_citizens(citizens)
    citizens = assign_families(citizens, minimum_sireing_gap)

    return citizens

def give_positions(positions, citizens):
    # camarilla_citizens = [x for x in citizens if x.faction == 'Camarilla']
    # max(camarilla_citizens, key=attrgetter('age')).position = 'Prince'

    # Order citizen according to age
    citizens.sort(key=lambda x: x.age, reverse=True)

    for citizen in citizens:
        faction_positions = positions[citizen.faction]
        faction_ranks = get_faction_ranks(faction_positions)
        for rank in faction_ranks:
            # print('rank ' + str(rank))
            for position in faction_positions:
                if citizen.position == None:
                    if position_requirement_check(position, faction_positions, rank, citizens, citizen):
                        citizen.position = str(position)
                        # print(citizen.name + ' final position ' + position)

    return citizens

def get_faction_ranks(positions):
    ranks = []
    for position in positions:
        if positions[position]['Rank'] not in ranks:
            ranks.append(int(positions[position]['Rank']))
    ranks.sort()

    return ranks

def position_requirement_check(position, faction_positions, rank, citizens, citizen):
    if faction_positions[position]['Clan_restriction'] == False:
        clan_critrion = True
    else:
        if len([x for x in citizens if x.clan == citizen.clan and x.position == position and x.name != citizen.name]) < faction_positions[position]['Number_allowed']:
            clan_critrion = True
        else:
            clan_critrion = False

    correct_rank = True if faction_positions[position]['Rank'] == rank else False

    n_positions_in_city = len([x for x in citizens if x.position == position])
    position_is_open = True if n_positions_in_city < faction_positions[position]['Number_allowed'] else False

    check_result = True if correct_rank and position_is_open and clan_critrion else False

    return check_result

def relate_citizens(citizens, ):
    with open(FILE_CITIZEN_RELATIONS) as json_file:
        relation_options = json.load(json_file)

        for citizen in citizens:
            new_relation_dict = {}
            for other_citizen in citizens:
                if other_citizen != citizen:
                    new_relation_dict[other_citizen.name] = random.choice(relation_options)
            citizen.relations = new_relation_dict

    return citizens

def assign_families(citizens, minimum_sireing_gap):
    clan_list = get_clans(citizens)

    for clan in clan_list:
        clan_members = [x for x in citizens if x.clan == clan]
        clan_members.sort(key=lambda x: x.age, reverse=True)
        if len(clan_members) > 1:
            for clan_member in clan_members:
                for other_clan_member in clan_members:
                    # Looking for 
                    if other_clan_member.sire == None and clan_member.age - other_clan_member.age > minimum_sireing_gap:
                        other_clan_member.sire = clan_member.name
                        clan_member.children.append(other_clan_member.name)

    return citizens
            

def get_clans(citizens):
    clans = []
    for citizen in citizens:
        if citizen.clan not in clans:
            clans.append(str(citizen.clan))

    return clans

def make_csv(citizens):
    with open('city.csv', 'wb') as csv_file:
        wr = csv.writer(csv_file, delimiter=',')
        for citizen in citizens:
            wr.writerow(list(citizen))

new_city = generate_random_city()

for dweller in new_city:
    print('name: ' + str(dweller.name) + ' ' + 'sire: ' + str(dweller.sire) + ' ' + 'children: ' + str(dweller.children))


# pprint.pprint(generate_random_city())

# make_csv(generate_random_city())



