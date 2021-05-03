import default_data

def flatten_dictionary(input_dictionary):
    result = {}
    for main_property, detail in input_dictionary.items():
        if isinstance(detail, dict):
            for sub_property, sub_detail in detail.items():
                result[sub_property] = sub_detail
        else:
            result[main_property] = detail

    return result

def merge_dictionaries(dictionary_a, dictionary_b):
    merged_dictionary = {**dictionary_a, **dictionary_b}
    return merged_dictionary

def stat_block_for_flask_table(number_of_stat_key_value_pairs,
                               dictionary_container,
                               current_table,
                               number_of_cols):
    # dictionary with n number of  lists for values and keys, names as keys1 = [...], values1 =[...]
    stat_lists_container = {}
    
    level_counter = 1
    for level1 in dictionary_container.keys():

        stat_list_value_name = "keys" + str(level_counter)
        stat_list_key_name = "values" + str(level_counter)

        stat_list_keys = list(dictionary_container[level1].keys())
        stat_list_values = list(dictionary_container[level1].values())

        stat_lists_container[stat_list_value_name] = stat_list_keys
        stat_lists_container[stat_list_key_name] = stat_list_values
        
        level_counter = level_counter +1

    # get largest dictionary + its length
    longest_sub_dictinary = {}
    for sub_dictionary_key in dictionary_container.keys():
        if len(dictionary_container[sub_dictionary_key]) > len(longest_sub_dictinary):
            longest_sub_dictinary = dictionary_container[sub_dictionary_key]
    number_of_rows = len(longest_sub_dictinary)

    for current_row in range(1, number_of_rows + 1):
        row_stat_block = {}
        current_value_pair = 1
        
        for current_col in range(1, (number_of_stat_key_value_pairs * 2) + 1):

            if current_col % 2 != 0:
                if current_row > len(stat_lists_container['keys' + str(current_value_pair)]):
                    stat_1 = ''
                else:
                    stat_1 = stat_lists_container['keys' + str(current_value_pair)][current_row-1]
                row_stat_block['col' + str(current_col)] = stat_1
                
                if current_row > len(stat_lists_container['values' + str(current_value_pair)]):
                    stat_2 = ''
                else:
                    stat_2 = stat_lists_container['values' + str(current_value_pair)][current_row-1]
                row_stat_block['col' + str(current_col + 1)] = stat_2
                
                current_value_pair = current_value_pair + 1

        while len(row_stat_block) < number_of_cols:
            row_stat_block['col' + str(len(row_stat_block) + 1)] = ''
        
        current_table.append(row_stat_block)
    
def dictionary_to_flask_table(character_dictionary):
    table = []
    # category separator rows
    row_character_details ={'col1': 'Character_Details',
                            'col2': "",
                            'col3': "",
                            'col4': "",
                            'col5': "",
                            'col6': ""}
    table.append(row_character_details)

    row_character_details_types = {'col1': 'Basic_Information',
                                   'col2': "",
                                   'col3': "Trackers",
                                   'col4': "",
                                   'col5': "",
                                   'col6': ""}
    table.append(row_character_details_types)
    
    stat_block_for_flask_table(number_of_stat_key_value_pairs=2,
                               dictionary_container=character_dictionary['Character_Details'],
                               current_table=table,
                               number_of_cols=6)


    row_attributes ={'col1': 'Attributes',
                     'col2': "",
                     'col3': "",
                     'col4': "",
                     'col5': "",
                     'col6': ""}
    table.append(row_attributes)

    row_attributes_types ={'col1': 'Physical_Attributes',
                           'col2': "",
                           'col3': "Social_Attributes",
                           'col4': "",
                           'col5': "Mental_Attributes",
                           'col6': ""}
    table.append(row_attributes_types)
    
    stat_block_for_flask_table(number_of_stat_key_value_pairs=3,
                            dictionary_container=character_dictionary['Attributes'],
                            current_table=table,
                            number_of_cols=6)        
    
    row_skills ={'col1': 'Skills',
                 'col2': "",
                 'col3': "",
                 'col4': "",
                 'col5': "",
                 'col6': ""}
    table.append(row_skills)   

    row_skills_types ={'col1': 'Physical_Skills',
                       'col2': "",
                       'col3': "Social_Skills",
                       'col4': "",
                       'col5': "Mental_Skills",
                       'col6': ""}
    table.append(row_skills_types)

    stat_block_for_flask_table(number_of_stat_key_value_pairs=3,
                            dictionary_container=character_dictionary['Skills'],
                            current_table=table,
                            number_of_cols=6)   

    row_disciplines ={'col1': 'Disciplines',
                      'col2': "",
                      'col3': "",
                      'col4': "",
                      'col5': "",
                      'col6': ""} 
    table.append(row_disciplines)

    row_disciplines_types ={'col1': 'Clan_Disciplines',
                            'col2': "",
                            'col3': "Non-Clan_Disciplines",
                            'col4': "",
                            'col5': "",
                            'col6': ""}
    table.append(row_disciplines_types)

    stat_block_for_flask_table(number_of_stat_key_value_pairs=2,
                            dictionary_container=character_dictionary['Disciplines'],
                            current_table=table,
                            number_of_cols=6)   

    return table

def form_structuring(gathered_form_data):
 
    gathered_values = {'manual_age': int(gathered_form_data['manual_age']),
                       'manual_clan': 'Malkavian' if gathered_form_data['manual_clan'] == 'Random' else gathered_form_data['manual_clan'],
                       'manual_sex': 'Female' if gathered_form_data['manual_sex'] == 'Random' else gathered_form_data['manual_sex'],
                       'manual_generation': 10 if gathered_form_data['manual_generation'] == 'Random' else int(gathered_form_data['manual_generation']),
                       'manual_name': gathered_form_data['manual_name']}

    gathered_weights = {'Attributes': int(gathered_form_data['Attributes']),
                        'Clan_Disciplines': int(gathered_form_data['Clan_Disciplines']),
                        'Disciplines': int(gathered_form_data['Disciplines']),
                        'Mental_Attributes': int(gathered_form_data['Mental_Attributes']),
                        'Mental_Skills': int(gathered_form_data['Mental_Skills']),
                        'Non-Clan_Disciplines': int(gathered_form_data['Non-Clan_Disciplines']),
                        'Physical_Attributes': int(gathered_form_data['Physical_Attributes']),
                        'Physical_Skills': int(gathered_form_data['Physical_Skills']),
                        'Skills': int(gathered_form_data['Skills']),
                        'Social_Attributes': int(gathered_form_data['Social_Attributes']),
                        'Social_Skills': int(gathered_form_data['Social_Skills'])}

    gathered_condition = {'manual_clan_condition': False if gathered_form_data['manual_clan']=='Random' else True,
                          'manual_generation_condition': False if gathered_form_data['manual_generation']=='Random' else True,
                          'manual_age_condition': False if gathered_form_data['manual_age_selection']=='Random' else True,
                          'manual_sex_condition': False if gathered_form_data['manual_sex']=='Random' else True,
                          'manual_name_condition': False if gathered_form_data['manual_name_selection']=='Random' else True}


    return gathered_condition, gathered_values, gathered_weights
