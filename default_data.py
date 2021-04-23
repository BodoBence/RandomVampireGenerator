def vampire_generator_simulated_input():
    input_values = {'manual_clan_condition': False,
                    'manual_generation_condition': False,
                    'manual_age_condition': False,
                    'manual_sex_condition': False,
                    'manual_name_condition': False,
                    'manual_age': 300,
                    'manual_clan': 'Malkavian',
                    'manual_sex': 'Female',
                    'manual_generation': 10,
                    'manual_name': "Fruzsi"}
   
    weight_values = {'Categories': {'Attributes': 30,
                                    'Skills': 30,
                                    'Disciplines': 30},
                     'Attributes': {'Physical_Attributes': 30,
                                    'Social_Attributes': 30, 
                                    'Mental_Attributes': 30},
                     'Skills': {'Physical_Skills': 30, 
                                'Social_Skills': 30, 
                                'Mental_Skills': 30},
                     'Disciplines': {'Clan_Disciplines': 70, 
                                     'Non-Clan_Disciplines': 20}}

    return input_values, weight_values

def basic_info_request_web_data():
    manual_clan_condition_details = {'type': 'checkbox',
                                     'default_value': 'false',
                                     'field_text': 'Select clan manually?'}
    manual_age_condition_details = {'type': 'checkbox',
                                     'default_value': 'false',
                                     'field_text': 'Select age manually?'}
    manual_generation_condition_details = {'type': 'checkbox',
                                           'default_value': 'false',
                                           'field_text': 'Select generation manually?'}
    manual_sex_condition_details = {'type': 'checkbox',
                                     'default_value': 'false',
                                     'field_text': 'Select sex manually?'}
    manual_name_condition_details = {'type': 'checkbox',
                                     'default_value': 'false',
                                     'field_text': 'Give name manually?'}
    manual_age_details = {'type': 'number',
                          'default_value': 300,
                          'field_text': 'Age:'}
    manual_generation_details = {'type': 'number',
                                 'default_value': 10,
                                 'field_text': 'Generation:'}
    manual_name_details = {'type': 'text',
                           'default_value': 'Default Daniel',
                           'field_text': 'Name:'}

    start_variables = {'manual_clan_condition': manual_clan_condition_details,
                       'manual_age_condition': manual_age_condition_details,
                       'manual_generation_condition' : manual_generation_condition_details,
                       'manual_sex_condition' : manual_sex_condition_details,
                       'manual_name_condition' : manual_name_condition_details,
                       'manual_age' : manual_age_details,
                       'manual_generation' : manual_generation_details,
                       'manual_name' : manual_name_details}
    return start_variables

def default_attibute_data():
    attributes_physical = {'Strength': 1,
                           'Dexterity': 1,
                           'Stamina': 1}
    attributes_social = {'Charisma': 1,
                         'Manipulation': 1,
                         'Composure': 1}
    attributes_mental = {'Intelligence': 1,
                         'Wits': 1,
                         'Resolve': 1}
    attributes = {'Physical_Attributes': attributes_physical,
                  'Social_Attributes': attributes_social,
                  'Mental_Attributes': attributes_mental}
    return attributes

def default_skill_data():
    skills_physical = {'Athletics': 0,
                    'Brawl': 0,
                    'Craft': 0,
                    'Drive': 0,
                    'Melee': 0,
                    'Firearms': 0,
                    'Larceny': 0,
                    'Stealth': 0,
                    'Survival': 0}
    skills_social = {'Animal Ken': 0,
                        'Etiquette': 0,
                        'Insight': 0,
                        'Intimidation': 0,
                        'Leadership': 0,
                        'Performance': 0,
                        'Persuasion': 0,
                        'Streetwise': 0,
                        'Subterfuge': 0}
    skills_mental = {'Academics': 0,
                        'Awareness': 0,
                        'Finance': 0,
                        'Investigation': 0,
                        'Medicine': 0,
                        'Occult': 0,
                        'Politics': 0,
                        'Science': 0,
                        'Technology': 0}
    skills = {'Physical_Skills': skills_physical,
              'Social_Skills': skills_social,
              'Mental_Skills': skills_mental}
    
    return skills

def default_discipline_data():
    disciplines = {'Celerity': 0,
                   'Fortitude': 0,
                   'Potence': 0,
                   'Dominate': 0,
                   'Obfuscate': 0,
                   'Presence': 0,
                   'Auspex': 0,
                   'Blood Sorcery': 0,
                   'Thinblood Alchemy': 0,
                   'Oblivion': 0,
                   'Animalism': 0,
                   'Protean': 0}
    return disciplines

def default_generation_based_point_data():
    generation_based_point_max ={1:10,
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
    xp_costs = {'Attributes': 5, 
                 'Skills': 3,
                 'Disciplines': {'Clan_Disciplines': 5,
                                 'Non-Clan_Disciplines': 7}}
    return xp_costs

def default_weights_data():
    weight_categories = {'Attributes': 20, 'Skills': 40, 'Disciplines': 10}
    weight_attributes = {'Physical_Attributes': 10, 'Social_Attributes': 25, 'Mental_Attributes': 10}
    weight_skills = {'Physical_Skills': 20, 'Social_Skills': 20, 'Mental_Skills': 10}
    weight_disciplines =  {'Clan_Disciplines': 4, 'Non-Clan_Disciplines': 1}

    weight_values = {'Categories': weight_categories,
                     'Attributes': weight_attributes,
                     'Skills': weight_skills,
                     'Disciplines': weight_disciplines}

    return weight_values

def default_clan_disciplines_data():
    clan_disciplines = {'Banu Haqim': ['Celerity', 'Obfuscate', 'Blood Sorcery'],
                        'Brujah': ['Potence', 'Celerity', 'Presence'],
                        'Gangrel': ['Fortitude', 'Animalism', 'Protean'],
                        'Lasombra': ['Domnaite', 'Potence', 'Oblivion'],
                        'Malkavian': ['Obfuscate', 'Auspex', 'Dominate'],
                        'Ministry': ['Obfuscate', 'Protean', 'Presence'],
                        'Nosferatu': ['Obfuscate', 'Animalism', 'Potence'],
                        'Ravnos': ['Animalism', 'Obfuscate', 'Presence'],
                        'Toreador': ['Celerity', 'Auspex', 'Presence'],
                        'Tremere': ['Auspex', 'Blood Sorcery', 'Dominate'],
                        'Tzimische': ['Animalism', 'Auspex', 'Protean'],
                        'Ventrue': ['Dominate', 'Prsence', 'Fortitude'],
                        'Hecata': ['Auspex', 'Fortitude', 'Oblivion']}
    return clan_disciplines

def default_clans_data():
    clans = ['Banu Haqim',
             'Brujah',
             'Gangrel',
             'Lasombra',
             'Malkavian',
             'Ministry',
             'Nosferatu',
             'Ravnos',
             'Toreador',
             'Tremere',
             'Tzimische',
             'Ventrue',
             'Hecata']
    return clans

def default_generations_data():
    generations = range(1, 17)
    return generations

def default_ages_data():
    ages = range(1, 3001)
    return ages

def default_sexes_data():
    sexes = ['Male', 'Female']
    return sexes