# Random Vampire Generator

import random
import default_data
import pprint

def convert_txt_to_string_list(filename, listname):
    with open(filename) as inf:
        listname = inf.readlines()
        listname = [name.strip() for name in listname]
    return listname

def select_from_list(options, condition, user_defined):
    if condition == False:
        selected = random.choice(options)
        to_return = selected
    else:
        to_return = user_defined
    return to_return

def create_name(sex, male_names, female_names, surnames, name_selection_critera, manual_name):
    name_surname = select_from_list(options=surnames,
                                    condition=name_selection_critera,
                                    user_defined=manual_name)
    
    if sex == 'Female':
        name_christian = select_from_list(options=female_names,
                                          condition=name_selection_critera,
                                          user_defined=manual_name)
    else:
        name_christian = select_from_list(options=male_names,
                                          condition=name_selection_critera,
                                          user_defined=manual_name)
    name_full = name_christian + ', ' + name_surname
    return name_full
    
def setup_character_sheet(basic_info):
    character_sheet = {}
    character_sheet['Basic Information'] = basic_info
    character_sheet['Attributes'] = default_data.default_attibute_data()
    character_sheet['Skills'] = default_data.default_skill_data()
    character_sheet['XP Left'] = 0

    character_sheet['Disciplines'] = {}
    character_sheet['Disciplines']['Clan Disciplines'] = {}
    character_sheet['Disciplines']['Non-clan Disciplines'] = {}
    clan_disciplines = default_data.default_clan_disciplines_data()
    current_clan_disciplines = clan_disciplines[basic_info['Clan']]
    disciplines = default_data.default_discipline_data()

    for discipline in disciplines:
        if discipline in current_clan_disciplines:
            character_sheet['Disciplines']['Clan Disciplines'][discipline] = 0
        else:
            character_sheet['Disciplines']['Non-clan Disciplines'][discipline] = 0
    return character_sheet

def calculate_xp_points (age, gen):
    xp_points = max(300, round(age * (1/gen) * 22))
    return xp_points

def calculate_xp_cost(current_level, cost):
    xp_cost = (current_level + 1) * cost
    return xp_cost

def calculate_weights(weight_values):
    weights = {}
    for weight_group_type in weight_values.keys():
        weights[weight_group_type] = []
    
    for weight_group_type, weight_group_details in weight_values.items():
        for stat_type, weight in weight_group_details.items():
            for i in range(weight):
                weights[weight_group_type].append(stat_type)

    return weights

def generate_characters(character_sheet, weight_values):
    # Variable setup
    generation_data = default_data.default_generation_based_point_data()
    points_maximum = generation_data[character_sheet['Basic Information'].get('Generation')]
    clan_disciplines = default_data.default_clan_disciplines_data()
    weights = calculate_weights(weight_values)
    xp = calculate_xp_points(character_sheet['Basic Information'].get('Age'), 
                                character_sheet['Basic Information'].get('Generation'))
    xp_costs = default_data.default_costs_data()
    clan = character_sheet['Basic Information']['Clan']
    xp_stagnation_counter = []

    while xp > 2 and len(xp_stagnation_counter) < 50:
        current_category = random.choice(weights['Categories'])
        current_type = random.choice(weights[current_category])
        current_stat = random.choice(list(character_sheet[current_category][current_type].keys()))
        current_level = character_sheet[current_category][current_type][current_stat]

        # check is stat can be developed
        if current_level == points_maximum:
            xp_stagnation_counter.append(1)
            continue
        else:
             xp_stagnation_counter = []
        
        # special case for discipline development
        if current_category == 'Disciplines':
            if current_stat in clan_disciplines[clan]:
                cost = xp_costs[current_category]['Clan Disciplines']
            else:
                cost = xp_costs[current_category]['Non-clan Disciplines']
        else:
            cost = xp_costs[current_category]
        
        expense = calculate_xp_cost(current_level, cost)

        # spend xp if there is enough
        if expense < xp:
            character_sheet[current_category][current_type][current_stat] = current_level + 1
            xp = xp - expense
            xp_stagnation_counter.clear()
        else:
            xp_stagnation_counter.append(1)
        
        character_sheet['XP Left'] = xp

def clean_up_character(character_sheet):
    for discipline_type, disciplines_details in character_sheet['Disciplines'].items():
        character_sheet['Disciplines'][discipline_type] = {discipline:discipline_level for discipline,discipline_level in disciplines_details.items() if discipline_level != 0}

# fill charactersheet with stats and xp,send xp
def generate(input_data, weights_data):
    # Manual / Random imput data
    # MANUAL_CLAN_SELECTION = input_data['MANUAL_CLAN_SELECTION']
    # MANUAL_GENERATION_SELECTION = input_data['MANUAL_GENERATION_SELECTION']
    # MANUAL_AGE_SELECTION = input_data['MANUAL_AGE_SELECTION']
    # MANUAL_SEX_SELECTION = input_data['MANUAL_SEX_SELECTION']
    # MANUAL_NAME_SELECTION = input_data['MANUAL_NAME_SELECTION']

    # # Manual input data
    # CHOSEN_CLAN = input_data['CHOSEN_CLAN']
    # CHOSEN_GENERATION = input_data['CHOSEN_GENERATION']
    # CHOSEN_AGE = input_data['CHOSEN_AGE']
    # CHOSEN_SEX = input_data['CHOSEN_SEX']
    # CHOSEN_NAME = input_data['CHOSEN_NAME']

    # Acessing name lists
    file_names_male = 'names_male.txt'
    file_names_female = 'names_female.txt'
    file_names_surname = 'names_interesting.txt'
    names_male = []
    names_female = []
    names_surname = []

    names_male = convert_txt_to_string_list(file_names_male, names_male)
    names_female = convert_txt_to_string_list(file_names_female, names_female)
    names_surname = convert_txt_to_string_list(file_names_surname, names_surname)

    clan = select_from_list(options=default_data.default_clans_data(),
                            condition=input_data['manual_clan_condition'],
                            user_defined=input_data['manual_clan'])
  
    generation = select_from_list(options=default_data.default_generations_data(),
                                  condition=input_data['manual_generation_condition'],
                                  user_defined=input_data['manual_generation'])

    age = select_from_list(options=default_data.default_ages_data(),
                           condition=input_data['manual_age_condition'] ,
                           user_defined=input_data['manual_age'])

    sex = select_from_list(options=default_data.default_sexes_data(),
                           condition=input_data['manual_sex_condition'] ,
                           user_defined=input_data['manual_sex'])

    name = create_name(sex=sex,
                       male_names=names_male,
                       female_names=names_female,
                       surnames=names_surname,
                       name_selection_critera=input_data['manual_name_condition'],
                       manual_name=input_data['manual_name'])

    basic_info = {'Name': name,
                'Sex': sex,
                'Generation': generation,
                'Clan': clan,
                'Sire': 'Older Random Vampire',
                'Age': age }
  
    character_sheet = setup_character_sheet(basic_info)
    generate_characters(character_sheet, weights_data)
    clean_up_character(character_sheet)
    return character_sheet

input_values, weight_values = default_data.vampire_generator_simulated_input()
pprint.pprint(generate(input_values, weight_values))