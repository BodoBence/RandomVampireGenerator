# Random Vampire Generator
from flaskr.default_data import MAX_AGE
import random
import pprint
import default_data

def derangement_check(basic_info):
    if basic_info['Clan'] == 'Malkavian':
        basic_info['Derangement'] = default_data.get_derangement()
    else:
        basic_info.pop('Derangement')

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
                                                        'Blood_Potency': 0,
                                                        'XP_Used': 0}
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
                                                                              'Skills': {}}
        else:
            character_sheet['Disciplines']['Non-Clan_Disciplines'][discipline] = {'Level': 0,
                                                                                  'Skills': {}}
    return character_sheet

def calculate_age_modulated_weight (age):
    base_attribute_weight = 1
    base_skill_weight = 1
    base_discipline_weight = 1


    # must be higher than the base value
    changed_attribute = 2
    changed_skill = 1
    changed_discipline = 3

    changed_attribute_weight = int(base_attribute_weight + ((changed_attribute - base_attribute_weight) * (age / MAX_AGE)))
    changed_skill_weight = int(base_skill_weight + ((changed_skill - base_skill_weight) * (age / MAX_AGE)))
    changed_discipline_weight = int(base_attribute_weight + ((changed_discipline - base_discipline_weight) * (age / MAX_AGE)))

    changed_weights = {
        'Attributes': changed_attribute_weight,
        'Skills': changed_skill_weight,
        'Disciplines': changed_discipline_weight,}

    return changed_weights

def calculate_xp_points(age, generation, max_age, manual_calculation_condition, manual_xp):
    if manual_calculation_condition:

        xp_points = manual_xp

    else:

        xp_points = 0
        yearly_xp_base = 3
        min_xp = 300

        for i in range(age):

            yearly_xp = yearly_xp_base - (yearly_xp_base * (i / max_age))

            xp_points = xp_points + yearly_xp
        print(xp_points)
        xp_points = max(min_xp, xp_points)
        

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

# Fill Weights for Category selection
    fill_list_n_times_with_input(
        input_list=weights['Categories'],
        n=weight_values['Attributes'],
        custom_input='Attributes')

    fill_list_n_times_with_input(
        input_list=weights['Categories'],
        n=weight_values['Skills'],
        custom_input='Skills')

    fill_list_n_times_with_input(
        input_list=weights['Categories'],
        n=weight_values['Disciplines'],
        custom_input='Disciplines')

# Fill Weights for Attribute selection
    fill_list_n_times_with_input(
        input_list=weights['Attributes'],
        n=weight_values['Physical'],
        custom_input='Physical_Attributes')

    fill_list_n_times_with_input(
        input_list=weights['Attributes'],
        n=weight_values['Social'],
        custom_input='Social_Attributes')

    fill_list_n_times_with_input(
        input_list=weights['Attributes'],
        n=weight_values['Mental'],
        custom_input='Mental_Attributes')

# Fill Weights for Skill selection
    fill_list_n_times_with_input(
        input_list=weights['Skills'],
        n=weight_values['Physical'],
        custom_input='Physical_Skills')

    fill_list_n_times_with_input(
        input_list=weights['Skills'],
        n=weight_values['Social'],
        custom_input='Social_Skills')

    fill_list_n_times_with_input(
        input_list=weights['Skills'],
        n=weight_values['Mental'],
        custom_input='Mental_Skills')

# Fill Weights for Discipline selection
    fill_list_n_times_with_input(
        input_list=weights['Disciplines'],
        n=weight_values['Clan_Disciplines'],
        custom_input='Clan_Disciplines')

    fill_list_n_times_with_input(
        input_list=weights['Disciplines'],
        n=weight_values['Non-Clan_Disciplines'],
        custom_input='Non-Clan_Disciplines')

    return weights

def level_up(character_sheet, weight_values, input_conditions, input_values):
    # Variable setup
    generation_data = default_data.default_generation_based_point_data()
    points_maximum = generation_data[character_sheet['Character_Details']['Basic_Information']['Generation']]
    weights = calculate_weights(weight_values)
    xp = int(calculate_xp_points(age=character_sheet['Character_Details']['Basic_Information']['Age'],
                                 generation=character_sheet['Character_Details']['Basic_Information']['Generation'],
                                 max_age=default_data.MAX_AGE,
                                 manual_calculation_condition=input_conditions['manual_calculation_condition'],
                                 manual_xp=input_values['manual_calculation']))

    #Store Character xp
    character_sheet['Character_Details']['Trackers']['XP_Used'] = int(xp)

    xp_costs = default_data.default_costs_data()
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
                if level == points_maximum:
                    most_expensive_viable_level = level
                else:
                    if (level + 1) * clan_multiplier <= xp:
                        most_expensive_viable_level = level + 1

            if most_expensive_viable_level != 0:
                # get potential upgrade skills
                current_discipline_skills = list(character_sheet[current_category][current_type][current_stat]['Skills'].keys())
                potential_discipline_skills = []
                discipline_skill_dictionary = default_data.get_discipline_skills_and_rituals()[current_stat]['skill']
                for skill_level in discipline_skill_dictionary.keys():
                    if int(skill_level) <= most_expensive_viable_level:
                        for skill, description in discipline_skill_dictionary[skill_level].items():
                            if skill not in current_discipline_skills:
                                skill_info = (int(skill_level), skill, description)
                                potential_discipline_skills.append(skill_info)

                if len(potential_discipline_skills) == 0:
                    xp_stagnation_counter.append(1)
                    continue

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

def clean_up_character(character_sheet):
    disciplines_to_remove = {discipline_type: [] for discipline_type in character_sheet['Disciplines'].keys()}

    for discipline_type, disciplines_type_details in character_sheet['Disciplines'].items():
        for discipline in disciplines_type_details.keys():
            if character_sheet['Disciplines'][discipline_type][discipline]['Level'] == 0:
                disciplines_to_remove[discipline_type].append(discipline)

    # print('keys_to_remove', disciplines_to_remove)

    for discipline_type, disciplines in disciplines_to_remove.items():
        for discipline in disciplines:
            del character_sheet['Disciplines'][discipline_type][discipline]

# fill charactersheet with stats and xp,send xp
def generate(input_values, input_conditions, input_weights):
    names_male = []
    names_female = []
    names_surname = []

    names_male = convert_txt_to_string_list(default_data.FILE_NAMES_MALE, names_male)
    names_female = convert_txt_to_string_list(default_data.FILE_NAMES_FEMALE, names_female)
    names_surname = convert_txt_to_string_list(default_data.FILE_NAMES_INTERESTING, names_surname)

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
    level_up(character_sheet, input_weights, input_conditions, input_values)
    calculate_metrics(character_sheet)
    clean_up_character(character_sheet)

    return character_sheet

# uncomment for simluation input testing

# input_values = default_data.start_values()
# input_conditions = default_data.start_conditions()
# input_weights = default_data.start_weights()
# character_sheet = generate(input_values, input_conditions, input_weights)
# pprint.pprint(character_sheet)