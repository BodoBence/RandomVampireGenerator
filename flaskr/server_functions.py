import default_data
import os
import pprint
import json

script_dir = os.path.dirname(__file__)
FILE_CITY_GENERATOR_DEFAULT_INPUTS = os.path.join(script_dir, 'static', 'data', 'city_generator_default_inputs.json')

def get_maximum_skill_level(character_dictionary):

    generation = character_dictionary['Character_Details']['Basic_Information']['Generation']
    maximum_skill_level = default_data.default_generation_based_point_data()[generation]

    return maximum_skill_level

def form_structuring(gathered_form_data):

    gathered_values = {
        'manual_age': int(gathered_form_data['manual_age']),
        'manual_clan': 'Malkavian' if gathered_form_data['manual_clan'] == 'Random' else gathered_form_data['manual_clan'],
        'manual_sex': 'Female' if gathered_form_data['manual_sex'] == 'Random' else gathered_form_data['manual_sex'],
        'manual_generation': default_data.start_values()['manual_generation'] if gathered_form_data['manual_generation'] == 'Random' else int(gathered_form_data['manual_generation']),
        'manual_name': gathered_form_data['manual_name'],
        'manual_calculation': int(gathered_form_data['manual_calculation'])}

    gathered_weights = {
        'Attributes': default_data.start_weights()['Attributes'],
        'Skills': default_data.start_weights()['Skills'],
        'Disciplines': default_data.start_weights()['Disciplines'],

        'Clan_Disciplines':  100-int(gathered_form_data['simplified_discipline']),
        'Non-Clan_Disciplines': int(gathered_form_data['simplified_discipline']),
        'Mental': int(gathered_form_data['simplified_mental']),
        'Physical': int(gathered_form_data['simplified_physical']),
        'Social': int(gathered_form_data['simplified_social'])}


    gathered_condition = {
        'manual_clan_condition': False if gathered_form_data['manual_clan']=='Random' else True,
        'manual_generation_condition': False if gathered_form_data['manual_generation']=='Random' else True,
        'manual_age_condition': False if gathered_form_data['manual_age_selection']=='Random' else True,
        'manual_sex_condition': False if gathered_form_data['manual_sex']=='Random' else True,
        'manual_name_condition': False if gathered_form_data['manual_name_selection']=='Random' else True,
        'manual_calculation_condition': False if gathered_form_data['manual_calculation_selection']=='Algorithm' else True}


    return gathered_condition, gathered_values, gathered_weights

def structure_city(city):
    """ Create new neested structure for html display in grid:
    iterare through citizens in a hierarcy
    Faction –> Clan —> Rank -> Citizens """
    # Sort by faction
    city.sort(key=lambda x: x.faction)

    # Get lists of unique elements
    unique_factions = list(set([x.faction for x in city]))
    unique_clans_per_faction = {x:list(set([y.clan for y in city if y.faction == x])) for x in unique_factions}
    # Create and fill nested dicts with the new structure
    city_output = {}
    for faction in unique_factions:
        city_output[faction] = {} # Create new keys for the factions
        city_output[faction]['faction_leaders'] = {'1':[]} # Seperate custom nest for faction leaders
        for clan in unique_clans_per_faction[faction]:
            unique_ranks_per_clan = list(set([x.rank for x in city if x.faction == faction and x.clan == clan]))
            city_output[faction][clan] = {} # Create new keys for clans per faction
            for rank in unique_ranks_per_clan:
                if rank != 1: # Rank = 1 means faction leader, who go in under their own key ['faction_leaders'], not the clans
                    city_output[faction][clan][rank] = [] # Create new lists for ranks per clans per faction
                for citizen in city:
                    if citizen.faction == faction and citizen.clan == clan and citizen.rank == rank:
                        if citizen.rank == 1:
                            city_output[faction]['faction_leaders']['1'].append(citizen) # Seems redundant, but will allow the html to iterate through all citizens in one go and speerate leaders at the same time
                        else:
                            city_output[faction][clan][rank].append(citizen) # Majority of cases
            if city_output[faction][clan] == {}:
                del city_output[faction][clan]


      
    return city_output

def get_default_city_values():
    """ Return JSON dict values """
    with open(FILE_CITY_GENERATOR_DEFAULT_INPUTS) as json_file:
        values = json.load(json_file)
    return values 