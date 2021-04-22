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
    attributes = {'Physical': attributes_physical,
                  'Social': attributes_social,
                  'Mental': attributes_mental}
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
    skills = {'Physical': skills_physical,
              'Social': skills_social,
              'Mental': skills_mental}
    
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
                 'Disciplines': {'clan': 5,
                                 'non_clan': 7}}
    return xp_costs

def default_weights_data():
    weight_categories = {'Attributes': 20, 'Skills': 40, 'Disciplines': 10}
    weight_attributes = {'Physical': 10, 'Social': 25, 'Mental': 10}
    weight_skills = {'Physical': 20, 'Social': 20, 'Mental': 10}
    weight_disciplines =  {'Clan': 4, 'Non-clan': 1}

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