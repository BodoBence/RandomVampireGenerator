import pprint
import random
import os
import json
import uuid

from dataclasses import dataclass
from operator import attrgetter


SCRIPT_DIR = os.path.dirname(__file__)
FILE_FACTIONS = os.path.join(SCRIPT_DIR, 'static', 'factions.json')
FILE_FACTION_AFILIATIONS = os.path.join(SCRIPT_DIR, 'static', 'faction_afiliations.json')
FILE_POSITIONS = os.path.join(SCRIPT_DIR, 'static', 'positions.json')
FILE_CITIZEN_RELATIONS = os.path.join(SCRIPT_DIR, 'static', 'citizen_relations.json')
FILE_NAMES_MALE = os.path.join(SCRIPT_DIR, 'static', 'names_male.txt')
FILE_NAMES_FEMALE = os.path.join(SCRIPT_DIR, 'static', 'names_female.txt')
FILE_NAMES_INTERESTING = os.path.join(SCRIPT_DIR, 'static', 'names_interesting.txt')

def system_inputs():
    """ Inputs needed for city generation, but not controlled by the used """
    pass

def test_user_inputs():
    """ Manual user inputs for TESTING without having to interface, normally these should be gathered form the user """
    inputs = {
        'number_of_vampires': 20,
        'faction_ratio_camarilla': 10,
        'faction_ratio_sabbath': 4,
        'faction_ratio_anarch': 4,
        'faction_ratio_independent': 1,
        'age_average': 150,
        'age_standard_deviation': 120,
        'favor_females': 70,
        'favor_males': 30,
        'minimum_sireing_gap': 20
    }
    return inputs

def generate_random_city(
    faction_ratio_camarilla,
    faction_ratio_sabbath,
    faction_ratio_anarch,
    faction_ratio_independent,
    favor_females,
    favor_males,
    number_of_vampires,
    age_average,
    age_standard_deviation,
    minimum_sireing_gap):

    factions = create_factions_list(
        faction_ratio_camarilla,
        faction_ratio_sabbath,
        faction_ratio_anarch,
        faction_ratio_independent)

    sexes_list = ['Male' for i in range(1, favor_males)]
    female_list = ['Female' for i in range(1, favor_females)]
    sexes_list.extend(female_list)

    citizens = []
    # Generate citizens
    for citizen in range(number_of_vampires):
       citizens.append(generate_citizen(
            age_average, 
            age_standard_deviation, 
            factions,
            sexes_list))

    # Generate citizen relations
    citizens = create_citizen_relations(citizens, minimum_sireing_gap)

    return citizens

def create_factions_list(ratio_Camarilla, ratio_Sabbath, ratio_Anarch, ratio_Independent ):
    """ Weigh the factions from the JSON file according to their desired presence in the city """
    with open(FILE_FACTIONS) as json_file:
        factions = json.load(json_file)

    # apply weights to factions list
    weigted_list = []
    if ratio_Camarilla > 0:
        for i in range(1, ratio_Camarilla):
            weigted_list.append('Camarilla')
    if ratio_Anarch > 0:
        for i in range(1, ratio_Anarch):
            weigted_list.append('Anarch'),
    if ratio_Sabbath > 0:
        for i in range(1, ratio_Sabbath):
            weigted_list.append('Sabbath')
    if ratio_Independent > 0:
        for i in range(1, ratio_Independent):
            weigted_list.append('Independent')

    return weigted_list

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
    rank: int
    id: str

def generate_citizen(age_average, age_standard_deviation, factions, sexes):
    generated_age = abs(int(random.normalvariate(age_average, age_standard_deviation)))
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
        relations = None,
        rank = None,
        id = uuid.uuid1()
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
                        citizen.rank = rank
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
    """ Create sire - child relationships within clan member if there is enough age gap """
    # Create a list of the clans
    clan_list = []
    for citizen in citizens:
        if citizen.clan not in clan_list:
            clan_list.append(str(citizen.clan))

    # Sire–Child relationships by definitation can happen only within clans
    for clan in clan_list:
        clan_members = [x for x in citizens if x.clan == clan]  # Gather clan members
        clan_members.sort(key=lambda x: x.age, reverse=True)    # Sort clan member by age
        if len(clan_members) > 1:
            for potential_sire in clan_members:
                for potential_child in clan_members:
                    if potential_child.sire == None and potential_sire.age - potential_child.age > minimum_sireing_gap:
                        potential_child.sire = potential_sire.name
                        potential_sire.children.append(potential_child.name)

    return citizens


# new_city = generate_random_city()

# for dweller in new_city:
#     print('name: ' + str(dweller.name) + ' ' + 'sire: ' + str(dweller.sire) + ' ' + 'children: ' + str(dweller.children))

# pprint.pprint(generate_random_city())



