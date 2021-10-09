import pprint
import random
import os
import json
from dataclasses import dataclass
from operator import attrgetter

SCRIPT_DIR = os.path.dirname(__file__)
FILE_FACTIONS = os.path.join(SCRIPT_DIR, 'static', 'factions.json')
FILE_FACTION_AFILIATIONS = os.path.join(SCRIPT_DIR, 'static', 'faction_afiliations.json')
FILE_POSITIONS = os.path.join(SCRIPT_DIR, 'static', 'positions.json')
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
    citizens = create_citizen_relations(citizens)

    return citizens

def gather_default_input_values():
    inputs = {
        'number_of_vampires': 8,
        'number_of_factions': 3,
        'age_average': 150,
        'age_standard_deviation': 120,
        'favor_females': 70,
        'favor_males': 30
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
    name: str
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
        children = None,
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

def create_citizen_relations(citizens):
    with open(FILE_POSITIONS) as json_file:
        positions = json.load(json_file)    

    citizens = give_positions(positions, citizens)

    return citizens

def give_positions(positions, citizens):
    pprint.pprint(citizens)
    print('------------------------')
    # Camarilla
    camarilla_citizens = [x for x in citizens if x.faction == 'Camarilla']

    if len(camarilla_citizens) == 0:
        pass
    if len(camarilla_citizens) == 1:
        camarilla_citizens[0].position = 'Prince'
    if len(camarilla_citizens) > 1:
        # Assign a Prince
        max(camarilla_citizens, key=attrgetter('age')).position = 'Prince'

        # Assigin a Primogen Council
        camarilla_citizens = assign_primogen_council(camarilla_citizens)

    # Anarch
    anarch_citizens = [x for x in citizens if x.faction == 'Arnach']
    # Shabbath
    sabbath_citizens = [x for x in citizens if x.faction == 'Sabbath']
    # Independent
    independent_citizens = [x for x in citizens if x.faction == 'Independent']

    # Put all factions togther
    citizens_with_positions = []
    
    if len(camarilla_citizens) != 0:
        citizens_with_positions.append(camarilla_citizens)

    if len(anarch_citizens) != 0:
        citizens_with_positions.append(anarch_citizens)

    if len(sabbath_citizens) != 0:
        citizens_with_positions.append(sabbath_citizens)

    if len(independent_citizens) != 0:
        citizens_with_positions.append(independent_citizens)

    return citizens_with_positions
    
pprint.pprint(generate_random_city())