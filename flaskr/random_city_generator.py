import pprint
import random
import os
import json
import uuid
import default_data

from dataclasses import dataclass
from operator import attrgetter


SCRIPT_DIR = os.path.dirname(__file__)
FILE_FACTIONS = os.path.join(SCRIPT_DIR, 'static', 'factions.json')
FILE_FACTION_AFILIATIONS = os.path.join(SCRIPT_DIR, 'static', 'faction_afiliations.json')
FILE_POSITIONS = os.path.join(SCRIPT_DIR, 'static', 'positions.json')
FILE_CITIZEN_RELATIONS = os.path.join(SCRIPT_DIR, 'static', 'citizen_relations.json')
FILE_INTERNAL_INPUTS = os.path.join(SCRIPT_DIR, 'static', 'citiy_generator_internal_inputs.json')
FILE_NAMES_MALE = os.path.join(SCRIPT_DIR, 'static', 'names_male.txt')
FILE_NAMES_FEMALE = os.path.join(SCRIPT_DIR, 'static', 'names_female.txt')
FILE_NAMES_INTERESTING = os.path.join(SCRIPT_DIR, 'static', 'names_interesting.txt')

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

    with open(FILE_INTERNAL_INPUTS) as json_file:
        internal_inputs = json.load(json_file)
    
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
    for citizen in range(0, number_of_vampires):
        # print('generating vamp number: ' + str(citizen)) # DEBUG
        citizens.append(generate_citizen(
            age_average, 
            age_standard_deviation,
            internal_inputs['minimum_age'], 
            factions,
            sexes_list,
            internal_inputs['minimum_generation']))

    # Generate citizen relations
    citizens = create_citizen_relations(
        citizens, 
        minimum_sireing_gap, 
        internal_inputs['number_of_years_per_child'])

    # print('number of cirizens with relations: ' + str(len(citizens))) # DEBUG
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
    sire_in_city: bool
    blood_potency: int

def generate_citizen(age_average, age_standard_deviation, minimum_age, factions, sexes, minimum_generation):
    """ create a citizen class object and assign most of the values for its attributes """
    
    # The order of the following is important, as the later functions use the data of the earliers
    generated_age = max(minimum_age, abs(int(random.normalvariate(age_average, age_standard_deviation))))
    generated_sex = random.choice(sexes)
    generated_name = create_name(generated_sex)
    generated_faction = random.choice(factions)
    generated_clan = create_clans_list(generated_faction)[0]
    generated_generation = assign_generation(generated_age, generated_clan, age_average, minimum_generation)
    generated_blood_potency = int(random.choice(default_data.blood_potency_data()[str(generated_generation)]))

    generted_citizen = citizen(
        faction = generated_faction,
        position = None,
        age = generated_age,
        name = generated_name,
        sex =  generated_sex,
        clan = generated_clan,
        sire =  None,
        generation =  generated_generation,
        children = [],
        superior = None,
        relations = None,
        rank = None,
        id = uuid.uuid1(),
        sire_in_city = False,
        blood_potency = generated_blood_potency
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

def assign_generation(age, clan, age_average, minimum_generation):
    """ Pick a generation value based on age (seniority) and clan """
    # the lower the generation is the stronger, tipically older a vampire is
    if clan != 'Thin-blood': # Thin-blood have fewer generation options open to them
        generation_options = default_data.default_generations_data()
    else:
        generation_options = default_data.thinblood_generations_data()

    modulated_generation_options = [x for x in generation_options if x >= minimum_generation] # 1-6 generations are extremley rare, so we should exclude them
    age_bias = int((age / age_average) + 1) # the older the vampire is (relative to the average) the higher the bias
    generation = min([random.choice(modulated_generation_options) for i in range(0, age_bias)]) # the comparision of repeated random picks scews the choice toward a lower value

    return generation

def create_citizen_relations(citizens, minimum_sireing_gap, number_of_years_per_child):
    with open(FILE_POSITIONS) as json_file:
        positions = json.load(json_file)    

    citizens = give_positions(positions, citizens)
    # print('number of vamp after positions: ' + str(len(citizens))) # DEBUG
    citizens = relate_citizens(citizens)
    # print('number of vamp after relates: ' + str(len(citizens))) # DEBUG
    citizens = assign_families(citizens, minimum_sireing_gap, number_of_years_per_child)
    # print('number of vamp after families: ' + str(len(citizens))) # DEBUG
    citizens = create_non_city_sires(citizens)
    # print('number of vamp after nonsire: ' + str(len(citizens))) # DEBUG

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
                    if is_okay_to_take_position(position, faction_positions, rank, citizens, citizen):
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

def is_okay_to_take_position(position, faction_positions, rank, citizens, citizen):
    """ Determines if citizen can take position """

    # Check for other clan members with the same position
    if faction_positions[position]['Clan_restriction'] == False: # there can be more of this position in a clan
        clan_critrion_satisfied = True
    if faction_positions[position]['Clan_restriction'] == True: # there ce be ONLY ONE of this position in a clan
        if len([x for x in citizens if x.clan == citizen.clan and x.position == position and x.name != citizen.name]) < 1:
            clan_critrion_satisfied = True
        else:
            clan_critrion_satisfied = False

    # Check if the position has the correct rank
    correct_rank = True if faction_positions[position]['Rank'] == rank else False

    # Check if we wouldn't exceed the allowed number of citizens with the position
    n_positions_in_city = len([x for x in citizens if x.position == position])
    position_is_open = True if n_positions_in_city < faction_positions[position]['Number_allowed'] else False

    # Compare
    if correct_rank and position_is_open and clan_critrion_satisfied:
        return True
    else:
        return False

def relate_citizens(citizens, ):
    with open(FILE_CITIZEN_RELATIONS) as json_file:
        relation_options = json.load(json_file)

        for citizen in citizens:
            new_relation_dict = {}
            for other_citizen in citizens:
                if other_citizen != citizen:
                    new_relation_dict[other_citizen.name] = random.choice(relation_options)
            
            unique_ways_to_relate = list(set([x for x in new_relation_dict.values()]))
            new_relation_dict_formatted = {}
            for relation_way in unique_ways_to_relate:
                new_relation_dict_formatted[relation_way] = [x for x in new_relation_dict if new_relation_dict[x] == relation_way]

            citizen.relations = new_relation_dict_formatted

    return citizens

def assign_families(citizens, minimum_sireing_gap, number_of_years_per_child):
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
                    if is_okay_to_sire(potential_child, potential_sire, minimum_sireing_gap, number_of_years_per_child):
                        potential_child.sire = potential_sire.name
                        potential_child.sire_in_city = True
                        potential_sire.generation = potential_sire.generation + 1
                        potential_sire.children.append(potential_child.name)
    return citizens

def is_okay_to_sire(potential_child, potential_sire, minimum_sireing_gap, number_of_years_per_child):
    """ Check criteria for making sire – child relationships"""
    
    child_criterion = True if potential_child.sire == None else False
    age_criterion = True if potential_sire.age - potential_child.age > minimum_sireing_gap else False # Also exlcudes self to self matches
    sire_criterion = True if len(potential_sire.children) < (potential_sire.age / number_of_years_per_child) else False # Sire's can only make 1 child / 100 years

    if child_criterion and age_criterion and sire_criterion:
        return True
    else:
        return False

def create_non_city_sires(citizens):
    """ For citizens, whom getting a sire was not an option, give random named sires """
    for citizen in citizens:
        if citizen.sire_in_city == False:
            citizen.sire = create_name(random.choice(['Male', 'Female']))

    return citizens



# pprint.pprint(generate_random_city())



