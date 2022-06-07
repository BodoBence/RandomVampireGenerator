import csv
import json
import os
import random

script_dir = os.path.dirname(__file__)
FILE_NAMES_MALE = os.path.join(script_dir, 'static', 'names_male.txt')
FILE_NAMES_FEMALE = os.path.join(script_dir, 'static', 'names_female.txt')
FILE_NAMES_INTERESTING = os.path.join(script_dir, 'static', 'names_interesting.txt')
FILE_DISCIPLINE_SKILLS = os.path.join(script_dir, 'static', 'restructured_discipline_skills_rituals_ceremonies.json')
FILE_DERANGEMENTS = os.path.join(script_dir, 'static', 'derengements_curated.csv')
FILE_MAX_XPS = os.path.join(script_dir, 'static', 'max_xps.json')
FILE_CLANS = os.path.join(script_dir, 'static', 'clans.json')
FILE_DISCIPLINES = os.path.join(script_dir, 'static', 'disciplines.json')

MAX_AGE = 3000

# Character Generator
def start_conditions():
    start_conditions = {
        'manual_clan_condition': False,
        'manual_generation_condition': False,
        'manual_age_condition': False,
        'manual_sex_condition': False,
        'manual_name_condition': False,
        'manual_calculation_condition': False}
    return start_conditions

def start_values():
    start_values = {
        'manual_age': 1,
        'manual_clan': 'Malkavian',
        'manual_sex': 'Female',
        'manual_generation': 10,
        'manual_calculation': 1,
        'manual_name': "Fruzsi"}
    return start_values

def start_weights():
    start_weights = {
        'Attributes': 30,
        'Skills': 70,
        'Disciplines': 50,
        'Physical': 33,
        'Social': 33,
        'Mental': 33,
        'Clan_Disciplines': 100,
        'Non-Clan_Disciplines': 5}
    return start_weights

def age_modulated_weights():

    age_modulated_weights = {
        'Attributes': 40,
        'Skills': 70,
        'Disciplines': 90}
    
    return age_modulated_weights


def default_attibute_data():
    attributes_physical = {
        'Strength': 1,
        'Dexterity': 1,
        'Stamina': 1}
    attributes_social = {
        'Charisma': 1,
        'Manipulation': 1,
        'Composure': 1}
    attributes_mental = {
        'Intelligence': 1,
        'Wits': 1,
        'Resolve': 1}

    attributes = {
        'Physical_Attributes': attributes_physical,
        'Social_Attributes': attributes_social,
        'Mental_Attributes': attributes_mental}

    return attributes

def default_skill_data():
    skills_physical = {
        'Athletics': 0,
        'Brawl': 0,
        'Craft': 0,
        'Drive': 0,
        'Melee': 0,
        'Firearms': 0,
        'Larceny': 0,
        'Stealth': 0,
        'Survival': 0}

    skills_social = {
        'Animal Ken': 0,
        'Etiquette': 0,
        'Insight': 0,
        'Intimidation': 0,
        'Leadership': 0,
        'Performance': 0,
        'Persuasion': 0,
        'Streetwise': 0,
        'Subterfuge': 0}

    skills_mental = {
        'Academics': 0,
        'Awareness': 0,
        'Finance': 0,
        'Investigation': 0,
        'Medicine': 0,
        'Occult': 0,
        'Politics': 0,
        'Science': 0,
        'Technology': 0}

    skills = {
        'Physical_Skills': skills_physical,
        'Social_Skills': skills_social,
        'Mental_Skills': skills_mental}

    return skills

def default_discipline_data():
    disciplines = {
        'Celerity': 0,
        'Fortitude': 0,
        'Potence': 0,
        'Dominate': 0,
        'Obfuscate': 0,
        'Presence': 0,
        'Auspex': 0,
        'Blood_Sorcery': 0,
        'Oblivion': 0,
        'Animalism': 0,
        'Thin_Blood_Alchemy': 0,
        'Protean': 0}

    return disciplines

def expanded_disciplines(clan):
    disciplines = default_discipline_data()

    if clan == 'Thin-blood':
        disciplines['Thin_Blood_Alchemy'] = 0
    
    return disciplines

def default_generation_based_point_data():
    generation_based_point_max ={
        1:10,
        2:10,
        3:10,
        4:9,
        5:8,
        6:7,
        7:6,
        8:5,
        9:5,
        10:5,
        11:5,
        12:5,
        13:5,
        14:5,
        15:5,
        16:5}

    return generation_based_point_max

def default_costs_data():
    xp_costs = {
        'Attributes': 5,
        'Skills': 3,
        'Disciplines': {
            'Clan_Disciplines': 5,
            'Non-Clan_Disciplines': 7},
        'Rituals': 3,
        'Ceremonies': 3}
    return xp_costs

def default_clan_disciplines_data():
    clan_disciplines = {
        'Banu_Haqim': ['Celerity', 'Obfuscate', 'Blood_Sorcery'],
        'Brujah': ['Potence', 'Celerity', 'Presence'],
        'Gangrel': ['Fortitude', 'Animalism', 'Protean'],
        'Lasombra': ['Domnaite', 'Potence', 'Oblivion'],
        'Malkavian': ['Obfuscate', 'Auspex', 'Dominate'],
        'Ministry': ['Obfuscate', 'Protean', 'Presence'],
        'Nosferatu': ['Obfuscate', 'Animalism', 'Potence'],
        'Ravnos': ['Animalism', 'Obfuscate', 'Presence'],
        'Toreador': ['Celerity', 'Auspex', 'Presence'],
        'Tremere': ['Auspex', 'Blood_Sorcery', 'Dominate'],
        'Tzimische': ['Animalism', 'Dominate', 'Protean'],
        'Ventrue': ['Dominate', 'Prsence', 'Fortitude'],
        'Hecata': ['Auspex', 'Fortitude', 'Oblivion'],
        'Thin-blood': ['Thin_Blood_Alchemy']}

    return clan_disciplines

def default_clans_data():
    with open(FILE_CLANS) as json_file:
        clans = json.load(json_file)
        return clans

def default_disciplines_data():
    with open(FILE_DISCIPLINES) as json_file:
        disciplines = json.load(json_file)
        return disciplines

def default_generations_data():
    generations = range(3, 17)
    return generations

def thinblood_generations_data():
    generations = range(14, 17)
    return generations

def default_ages_data():
    ages = range(1, (MAX_AGE + 1))
    return ages

def default_sexes_data():
    sexes = ['Male', 'Female']
    return sexes

def get_discipline_skills_and_rituals():
    with open(FILE_DISCIPLINE_SKILLS) as json_file:
        discipline_skills_and_rituals = json.load(json_file)
    return discipline_skills_and_rituals

def blood_potency_data():
    blood_potency_correspondencies = {
        '1': [10],
        '2': list(range(9,11)),
        '3': list(range(8,11)),
        '4': list(range(5,11)),
        '5': list(range(4,10)),
        '6': list(range(3,9)),
        '7': list(range(3,8)),
        '8': list(range(2,7)),
        '9': list(range(2,6)),
        '10': list(range(1,5)),
        '11': list(range(1,5)),
        '12': list(range(1,4)),
        '13': list(range(1,4)),
        '14': [0],
        '15': [0],
        '16': [0],
        '17': [0],
        '18': [0]
    }

    return blood_potency_correspondencies

def get_derangement():
    with open(FILE_DERANGEMENTS) as chosen_file:
        reader = csv.reader(chosen_file)
        current_derangement = random.choice(list(reader))[0]
    return current_derangement

def get_max_xps():
    with open(FILE_MAX_XPS) as json_file:
        max_xps = json.load(json_file)
    return max_xps

# City Generator

def start_city_values():
    start_values = {
        'faction_ratio_camarilla': 10,
        'faction_ratio_anarch': 5,
        'faction_ratio_sabbath': 3,
        'faction_ratio_independent': 1,
        'age_average': 300,
        'age_standard_deviation': 120,
        'favor_males': 50,
        'manual_number_of_vampires': 10}

    return start_values