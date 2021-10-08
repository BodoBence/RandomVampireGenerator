import pprint
import random
import os
import json

SCRIPT_DIR = os.path.dirname(__file__)
FILE_FACTIONS = os.path.join(SCRIPT_DIR, 'static', 'factions.json')
FILE_FACTION_AFILIATIONS = os.path.join(SCRIPT_DIR, 'static', 'faction_afiliations.json')
FILE_NAMES_MALE = os.path.join(SCRIPT_DIR, 'static', 'names_male.txt')
FILE_NAMES_FEMALE = os.path.join(SCRIPT_DIR, 'static', 'names_female.txt')
FILE_NAMES_INTERESTING = os.path.join(SCRIPT_DIR, 'static', 'names_interesting.txt')

def gather_default_input_values():
    inputs = {
        'number_of_vampires': 8,
        'number_of_factions': 1,
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
        'MANUAL_FACTION_CHOICE': True
    }
    return condtitions

def fill_list_n_times_with_input(input_list, n, custom_input):
    for i in range(1, n):
        input_list.append(custom_input)
    return input_list

def convert_txt_to_string_list(filename, listname):
    with open(filename) as inf:
        listname = inf.readlines()
        listname = [name.strip() for name in listname]
    return listname

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

def create_sexes_list(n_male, n_female):
    sexes_list = []
    fill_list_n_times_with_input(sexes_list, n_male, "Male")
    fill_list_n_times_with_input(sexes_list, n_female, "Female")

    return sexes_list

def create_factions_list(number_of_factions, faction_choice_condition, manual_factions_list):
    if faction_choice_condition == False:
        with open(FILE_FACTIONS) as json_file:
            factions = json.load(json_file)
            factions_list = random.sample(factions, number_of_factions)
    else:
        factions_list = manual_factions_list

    return factions_list
    
def create_clans_list(faction):
    with open(FILE_FACTION_AFILIATIONS) as json_file:
        clans = json.load(json_file)
        clans_list = random.sample(clans[faction], 1)
    return clans_list

def generate_citizen(inputs, factions, sexes):
    age = int(random.normalvariate(inputs['age_average'], inputs['age_standard_deviation']))
    sex = random.choice(sexes)
    name = create_name(sex)
    faction = random.choice(factions)
    clan = create_clans_list(faction)[0]

    citizen = {
    'Faction': faction,
    'Position': 'none',
    'Age': age,
    'Name': name,
    'Sex': sex,
    'Clan': clan,
    'Sire': 'none',
    'Generation': 'none',
    'Children': {}
    }
    
    return citizen

def create_citizen_relations(citizens):

    return citizens

def generate_random_city():
    city_generator_inputs = gather_default_input_values()
    city_generator_conditions = gather_input_conditions()
    city_generator_manual_values = gather_manual_input_values()

    factions = create_factions_list(
        city_generator_inputs['number_of_factions'],
        city_generator_conditions['MANUAL_FACTION_CHOICE'],
        city_generator_manual_values['factions']
    )

    sexes = create_sexes_list(
        city_generator_inputs['favor_females'],
        city_generator_inputs['favor_males'])

    citizens = {}
    
    # Generate citizens
    for citizen in range(city_generator_inputs['number_of_vampires']):
        citizens[citizen] = generate_citizen(
            city_generator_inputs,
            factions,
            sexes)

    # Generate citizen relations
    citizens = create_citizen_relations(citizens)

    return citizens

pprint.pprint(generate_random_city())