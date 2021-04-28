def input_form_results_post_care(gathered_user_input):
    input_values = {'manual_clan_condition': True if 'manual_clan_condition' in gathered_user_input.keys() else False,
                    'manual_generation_condition': True if 'manual_generation_condition' in gathered_user_input.keys() else False,
                    'manual_age_condition': True if 'manual_age_condition' in gathered_user_input.keys() else False,
                    'manual_sex_condition': True if 'manual_sex_condition' in gathered_user_input.keys() else False,
                    'manual_name_condition': True if 'manual_name_condition' in gathered_user_input.keys() else False,
                    'manual_age': int(gathered_user_input['manual_age']) if gathered_user_input['manual_age'] != '' else 300,
                    'manual_clan': gathered_user_input['manual_clan'] if gathered_user_input['manual_clan'] != '' else "Malkavian",
                    'manual_sex': gathered_user_input['manual_sex'] if gathered_user_input['manual_sex'] != '' else "Female",
                    'manual_generation': int(gathered_user_input['manual_generation']) if gathered_user_input['manual_generation'] != '' else 10,
                    'manual_name': gathered_user_input['manual_name'] if gathered_user_input['manual_name'] != '' else "Default Dampire"}
   
    weight_values = {'Categories': {'Attributes': int(gathered_user_input['Attributes']),
                                    'Skills': int(gathered_user_input['Skills']),
                                    'Disciplines': int(gathered_user_input['Disciplines'])},
                     'Attributes': {'Physical_Attributes': int(gathered_user_input['Physical_Attributes']),
                                    'Social_Attributes': int(gathered_user_input['Social_Attributes']), 
                                    'Mental_Attributes': int(gathered_user_input['Mental_Attributes'])},
                     'Skills': {'Physical_Skills': int(gathered_user_input['Physical_Skills']), 
                                'Social_Skills': int(gathered_user_input['Social_Skills']), 
                                'Mental_Skills': int(gathered_user_input['Mental_Skills'])},
                     'Disciplines': {'Clan_Disciplines': int(gathered_user_input['Clan_Disciplines']), 
                                     'Non-Clan_Disciplines': int(gathered_user_input['Non-Clan_Disciplines'])}}
    return input_values, weight_values

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

