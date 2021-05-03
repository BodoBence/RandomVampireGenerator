# Random Vampire Generator
import random
import default_data
import pprint
import csv
from csv import reader

def get_derangement():
    derengements = 'derengements_curated.csv'

    with open(derengements) as chosen_file:
        reader = csv.reader(chosen_file)
        current_derangement = random.choice(list(reader))
    return current_derangement

def derangement_check(basic_info):
    if basic_info['Clan'] == 'Malkavian':
        basic_info['Derangement'] = get_derangement()
    return basic_info


def calculate_metrics(character_sheet):
    character_sheet['Character_Details']['Trackers']['Health'] = character_sheet['Attributes']['Physical_Attributes']['Stamina'] + 3
    character_sheet['Character_Details']['Trackers']['Willpower'] = character_sheet['Attributes']['Social_Attributes']['Composure'] + character_sheet['Attributes']['Mental_Attributes']['Resolve']
    current_blood_potency_pool = default_data.blood_potency_data()[str(character_sheet['Character_Details']['Basic_Information']['Generation'])]
    character_sheet['Character_Details']['Trackers']['Blood_Potency'] = random.choice(current_blood_potency_pool)
    return character_sheet

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
    if name_selection_critera == True:
        name_full = manual_name
    else:
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
    character_sheet['Character_Details'] = {}
    character_sheet['Character_Details']['Basic_Information'] = basic_info
    character_sheet['Character_Details']['Trackers'] = {'XP_Left': 0,
                                                        'Health': 0,
                                                        'Willpower': 0,
                                                        'Blood_Potency': 0}
    character_sheet['Attributes'] = default_data.default_attibute_data()
    character_sheet['Skills'] = default_data.default_skill_data()
    character_sheet['Disciplines'] = {}
    character_sheet['Disciplines']['Clan_Disciplines'] = {}
    character_sheet['Disciplines']['Non-Clan_Disciplines'] = {}
    clan_disciplines = default_data.default_clan_disciplines_data()
    current_clan_disciplines = clan_disciplines[basic_info['Clan']]
    disciplines = default_data.default_discipline_data()

    for discipline in disciplines:
        if discipline in current_clan_disciplines:
            character_sheet['Disciplines']['Clan_Disciplines'][discipline] = {'Level': 0,
                                                                              'Skills': {'': ''},
                                                                              'Rituals': {'': ''},
                                                                              'Ceremonies': {'': ''}}
        else:
            character_sheet['Disciplines']['Non-Clan_Disciplines'][discipline] = {'Level': 0,
                                                                                  'Skills': {'': ''},
                                                                                  'Rituals': {'': ''},
                                                                                  'Ceremonies': {'': ''}}
    return character_sheet

def calculate_xp_points(age):
    xp_points = max(300, (age * 2))
    return xp_points

def calculate_xp_cost_for_non_disciplines(current_level, cost):
    xp_cost = (current_level + 1) * cost
    return xp_cost

def fill_list_n_times_with_input(input_list, n, custom_input):
    for i in range(1, n):
        input_list.append(custom_input)
    return input_list

def calculate_weights(weight_values):
    weights = {'Categories': [],
               'Attributes': [],
               'Skills': [],
               'Disciplines': []}

    fill_list_n_times_with_input(input_list=weights['Categories'],
                                 n=weight_values['Attributes'],
                                 custom_input='Attributes')

    fill_list_n_times_with_input(input_list=weights['Categories'],
                                 n=weight_values['Skills'],
                                 custom_input='Skills')

    fill_list_n_times_with_input(input_list=weights['Categories'],
                                 n=weight_values['Disciplines'],
                                 custom_input='Disciplines')


    fill_list_n_times_with_input(input_list=weights['Attributes'],
                                 n=weight_values['Physical_Attributes'],
                                 custom_input='Physical_Attributes')

    fill_list_n_times_with_input(input_list=weights['Attributes'],
                                 n=weight_values['Social_Attributes'],
                                 custom_input='Social_Attributes')

    fill_list_n_times_with_input(input_list=weights['Attributes'],
                                 n=weight_values['Mental_Attributes'],
                                 custom_input='Mental_Attributes')  


    fill_list_n_times_with_input(input_list=weights['Skills'],
                                 n=weight_values['Physical_Skills'],
                                 custom_input='Physical_Skills')
    fill_list_n_times_with_input(input_list=weights['Skills'],
                                 n=weight_values['Social_Skills'],
                                 custom_input='Social_Skills')
    fill_list_n_times_with_input(input_list=weights['Skills'],
                                 n=weight_values['Mental_Skills'],
                                 custom_input='Mental_Skills')


    fill_list_n_times_with_input(input_list=weights['Disciplines'],
                                 n=weight_values['Clan_Disciplines'],
                                 custom_input='Clan_Disciplines')

    fill_list_n_times_with_input(input_list=weights['Disciplines'],
                                 n=weight_values['Non-Clan_Disciplines'],
                                 custom_input='Non-Clan_Disciplines')

    return weights      

def level_up(character_sheet, weight_values):
    # Variable setup
    generation_data = default_data.default_generation_based_point_data()
    points_maximum = generation_data[character_sheet['Character_Details']['Basic_Information'].get('Generation')]
    clan_disciplines = default_data.default_clan_disciplines_data()
    weights = calculate_weights(weight_values)
    xp = int(calculate_xp_points(character_sheet['Character_Details']['Basic_Information'].get('Age')))
    xp_costs = default_data.default_costs_data()
    clan = character_sheet['Character_Details']['Basic_Information']['Clan']
    xp_stagnation_counter = []
    
    while xp > 2 and len(xp_stagnation_counter) < 30:
        current_category = random.choice(weights['Categories'])
        current_type = random.choice(weights[current_category])
        current_stat = random.choice(list(character_sheet[current_category][current_type].keys()))
        if current_category == 'Disciplines':
            # Discipline track
            current_level = int(character_sheet[current_category][current_type][current_stat]['Level'])

            # get most expensive potential discipline skill level
            most_expensive_viable_level = 0 

            if current_type == 'Clan_Disciplines':
                clan_multiplier = default_data.default_costs_data()['Disciplines']['Clan_Disciplines']
            else:
                clan_multiplier = default_data.default_costs_data()['Disciplines']['Non-Clan_Disciplines']

            for level in range(0, current_level + 1 ):
                if (level + 1) * clan_multiplier <= xp:
                    most_expensive_viable_level = level + 1

            print(current_stat, most_expensive_viable_level)
            
            if most_expensive_viable_level != 0:
                # get potential upgrade skills
                current_discipline_skills = list(character_sheet[current_category][current_type][current_stat]['Skills'].keys())
                potential_discipline_skills = []
                for skill_level in default_data.get_discipline_skills_and_rituals()[current_stat].keys():
                    if int(skill_level) <= most_expensive_viable_level:
                        for skill, description in default_data.get_discipline_skills_and_rituals()[current_stat]['Skill'][skill_level].items():
                            if skill not in current_discipline_skills:
                                skill_info = (skill_level, skill, description)
                                potential_discipline_skills.append(skill_info)

                future_level, future_skill, future_skill_description = random.choice(potential_discipline_skills)

                if future_level > current_level:
                    character_sheet[current_category][current_type][current_stat]['Level'] += 1
                
                character_sheet[current_category][current_type][current_stat]['Skills'][future_skill] = future_skill_description
                xp = xp - (clan_multiplier * future_level)
                
            else:
                xp_stagnation_counter.append(1)
                continue

        else:
            current_level = character_sheet[current_category][current_type][current_stat]
            # Non discipline track
            if current_level < points_maximum:
                expense = calculate_xp_cost_for_non_disciplines(current_level, xp_costs[current_category])
                if expense < xp:
                    character_sheet[current_category][current_type][current_stat] = current_level + 1
                    xp = xp - expense
                    xp_stagnation_counter.clear()
                else:
                    xp_stagnation_counter.append(1)
                    continue
            else:
                xp_stagnation_counter.append(1)
                continue

"""         # check is stat can be developed
        if current_level == points_maximum:
            xp_stagnation_counter.append(1)
            continue
        else:
            xp_stagnation_counter = []


        # special case for discipline development
        if current_category == 'Disciplines':
            if current_stat in clan_disciplines[clan]:
                cost = xp_costs[current_category]['Clan_Disciplines']
            else:
                cost = xp_costs[current_category]['Non-Clan_Disciplines']
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
        
        character_sheet['Character_Details']['Trackers']['XP_Left']= xp """

def clean_up_character(character_sheet):
    for discipline_type, disciplines_details in character_sheet['Disciplines'].items():
        character_sheet['Disciplines'][discipline_type] = {discipline:discipline_level for discipline,discipline_level in disciplines_details.items() if discipline_level != 0}

# fill charactersheet with stats and xp,send xp
def generate(input_values, input_conditions, input_weights):
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
                            condition=input_conditions['manual_clan_condition'],
                            user_defined=input_values['manual_clan'])
  
    generation = select_from_list(options=default_data.default_generations_data(),
                                  condition=input_conditions['manual_generation_condition'],
                                  user_defined=input_values['manual_generation'])

    age = select_from_list(options=default_data.default_ages_data(),
                           condition=input_conditions['manual_age_condition'] ,
                           user_defined=input_values['manual_age'])

    sex = select_from_list(options=default_data.default_sexes_data(),
                           condition=input_conditions['manual_sex_condition'] ,
                           user_defined=input_values['manual_sex'])

    name = create_name(sex=sex,
                       male_names=names_male,
                       female_names=names_female,
                       surnames=names_surname,
                       name_selection_critera=input_conditions['manual_name_condition'],
                       manual_name=input_values['manual_name'])

    basic_info = {'Name': name,
                  'Sex': sex,
                  'Generation': generation,
                  'Clan': clan,
                  'Sire': 'Older Vampire',
                  'Age': age, 
                  'Derangement': 'N/A'}

    basic_info = derangement_check(basic_info)
  
    character_sheet = setup_character_sheet(basic_info)
    level_up(character_sheet, input_weights)
    calculate_metrics(character_sheet)
    clean_up_character(character_sheet)
    return character_sheet

# uncomment for simluation input testing

input_values = default_data.start_values()
input_conditions = default_data.start_conditions()
input_weights = default_data.start_weights()
character_sheet = generate(input_values, input_conditions, input_weights)
#pprint.pprint(character_sheet)      