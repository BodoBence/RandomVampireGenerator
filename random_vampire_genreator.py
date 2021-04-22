# Random Vampire Generator

import random
import default_data
import pprint

# Manual / Random imput data
MANUAL_CLAN_SELECTION = False
MANUAL_GENERATION_SELECTION = True
MANUAL_AGE_SELECTION = True
MANUAL_SEX_SELECTION = False
MANUAL_NAME_SELECTION = False

# Manual input data
CHOSEN_CLAN = 'Malkavian'
CHOSEN_GENERATION = 10
CHOSEN_AGE = 1000
CHOSEN_SEX = 'Female'
CHOSEN_NAME = 'Default Daniel'

# Acessing name lists
FILE_NAMES_MALE = 'names_male.txt'
FILE_NAMES_FEMALE = 'names_female.txt'
FILE_NAMES_SURNAME = 'names_interesting.txt'
NAMES_MALE = []
NAMES_FEMALE = []
NAMES_SURNAME = []

def convert_txt_to_string_list(filename, listname):
    with open(filename) as inf:
        listname = inf.readlines()
        listname = [name.strip() for name in listname]
    return listname

NAMES_MALE = convert_txt_to_string_list(FILE_NAMES_MALE, NAMES_MALE)
NAMES_FEMALE = convert_txt_to_string_list(FILE_NAMES_FEMALE, NAMES_FEMALE)
NAMES_SURNAME = convert_txt_to_string_list(FILE_NAMES_SURNAME, NAMES_SURNAME)

def select_from_list(options, condition, user_defined):
    if condition == False:
        selected = random.choice(options)
        to_return = selected
    else:
        to_return = user_defined
    print(to_return)
    return to_return

SELECTED_CLAN = select_from_list(options=default_data.default_clans_data(),
                                 condition=MANUAL_CLAN_SELECTION,
                                 user_defined=CHOSEN_CLAN)
                                 
SELECTED_GENERATION = select_from_list(options=default_data.default_generations_data(),
                                       condition=MANUAL_GENERATION_SELECTION,
                                       user_defined=CHOSEN_GENERATION)

SELECTED_AGE = select_from_list(options=default_data.default_ages_data(),
                                condition=MANUAL_AGE_SELECTION ,
                                user_defined=CHOSEN_AGE)

SELECTED_SEX = select_from_list(options=default_data.default_sexes_data(),
                                condition=MANUAL_SEX_SELECTION ,
                                user_defined=CHOSEN_SEX)

def create_name(sex, male_names, female_names, surnames):
    default_name_surname = ''
    name_surname = select_from_list(options=surnames,
                                    condition=False,
                                    user_defined=default_name_surname)
    
    default_name_christian = ''
    if sex == 'Female':
        name_christian = select_from_list(options=female_names,
                                          condition=False,
                                          user_defined=default_name_christian)
    else:
        name_christian = select_from_list(options=male_names,
                                          condition=False,
                                          user_defined=default_name_christian)
    name_full = name_christian + ', ' + name_surname
    return name_full
    
SELECTED_NAME = create_name(sex=SELECTED_SEX,
                            male_names=NAMES_MALE,
                            female_names=NAMES_FEMALE,
                            surnames=NAMES_SURNAME)

BASIC_INFO = {'Name': SELECTED_NAME,
              'Sex': SELECTED_SEX,
              'Generation': SELECTED_GENERATION,
              'Clan': SELECTED_CLAN,
              'Sire': 'Older Random Vampire',
              'Age': SELECTED_AGE }

CHARACTER_SHEET = {}

def setup_character_sheet():
    CHARACTER_SHEET['Basic Information'] = BASIC_INFO
    CHARACTER_SHEET['Attributes'] = default_data.default_attibute_data()
    CHARACTER_SHEET['Skills'] = default_data.default_skill_data()
    CHARACTER_SHEET['XP Left'] = 0

    CHARACTER_SHEET['Disciplines'] = {}
    CHARACTER_SHEET['Disciplines']['Clan'] = {}
    CHARACTER_SHEET['Disciplines']['Non-clan'] = {}
    clan_disciplines = default_data.default_clan_disciplines_data()
    current_clan_disciplines = clan_disciplines[BASIC_INFO['Clan']]
    disciplines = default_data.default_discipline_data()

    for discipline in disciplines:
        if discipline in current_clan_disciplines:
            CHARACTER_SHEET['Disciplines']['Clan'][discipline] = 0
        else:
            CHARACTER_SHEET['Disciplines']['Non-clan'][discipline] = 0

def calculate_xp_points (age, gen):
    xp_points = max(300, round(age * (1/gen) * 22))
    return xp_points

def calculate_xp_cost(current_level, cost):
    xp_cost = (current_level + 1) * cost
    return xp_cost

def calculate_weights():
    weight_values = default_data.default_weights_data()
    weights = {}
    for weight_group_type in weight_values.keys():
        weights[weight_group_type] = []
    
    for weight_group_type, weight_group_details in weight_values.items():
        for stat_type, weight in weight_group_details.items():
            for i in range(weight):
                weights[weight_group_type].append(stat_type)

    return weights

def generate_characters():
    # Variable setup
    generation_data = default_data.default_generation_based_point_data()
    points_maximum = generation_data[BASIC_INFO.get('Generation')]
    clan_disciplines = default_data.default_clan_disciplines_data()
    weights = calculate_weights()
    xp = calculate_xp_points(BASIC_INFO.get('Age'), 
                                BASIC_INFO.get('Generation'))
    xp_costs = default_data.default_costs_data()
    clan = CHARACTER_SHEET['Basic Information']['Clan']
    xp_stagnation_counter = [1]

    while xp > 2 and len(xp_stagnation_counter) < 50:
        current_category = random.choice(weights['Categories'])
        current_type = random.choice(weights[current_category])
        current_stat = random.choice(list(CHARACTER_SHEET[current_category][current_type].keys()))
        current_level = CHARACTER_SHEET[current_category][current_type][current_stat]

        # check is stat can be developed
        if current_level == points_maximum:
            xp_stagnation_counter.append(1)
            continue
        
        # special case for discipline development
        if current_category == 'Disciplines':
            if current_stat in clan_disciplines[clan]:
                cost = xp_costs[current_category]['clan']
            else:
                cost = xp_costs[current_category]['non_clan']
        else:
            cost = xp_costs[current_category]
        
        expense = calculate_xp_cost(current_level, cost)

        # spend xp if there is enough
        if expense < xp:
            CHARACTER_SHEET[current_category][current_type][current_stat] = current_level + 1
            xp = xp - expense
            xp_stagnation_counter.clear()
        else:
            xp_stagnation_counter.append(1)
        
        CHARACTER_SHEET['XP Left'] = xp

def clean_up_character():
    for discipline_type, disciplines_details in CHARACTER_SHEET['Disciplines'].items():
        CHARACTER_SHEET['Disciplines'][discipline_type] = {discipline:discipline_level for discipline,discipline_level in disciplines_details.items() if discipline_level != 0}

# fill charactersheet with stats and xp,send xp
setup_character_sheet()
generate_characters()
clean_up_character()

pprint.pprint(CHARACTER_SHEET)