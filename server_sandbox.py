# import things
from flask import Flask, render_template
from flask_table import Table, Col
import default_data

app = Flask(__name__)

@app.route('/', )
def home():
    return table.__html__()

# Declare your table
class ItemTable(Table):
    col1 = Col('col1')
    col2 = Col('col2')
    col3 = Col('col3')
    col4 = Col('col4')
    col5 = Col('col5')
    col6 = Col('col6')

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

    print('stat_lists_container', stat_lists_container)
    print('number_of_rows', number_of_rows)
    print('number_of_stat_key_value_pairs', number_of_stat_key_value_pairs)

    for current_row in range(1, number_of_rows + 1):
        row_stat_block = {}
        current_value_pair = 1
        
        for current_col in range(1, (number_of_stat_key_value_pairs * 2) + 1):

            if current_col % 2 != 0:
                print('current_col',current_col)
                row_stat_block['col' + str(current_col)] = stat_lists_container['keys' + str(current_value_pair)][current_row-1]
                row_stat_block['col' + str(current_col + 1)] = stat_lists_container['values' + str(current_value_pair)][current_row-1]
                current_value_pair = current_value_pair + 1
                print('row_stat_block',row_stat_block)
        while len(row_stat_block) < number_of_cols:
            row_stat_block['col' + str(len(row_stat_block) + 1)] = ''
            
        print('row_stat_block', row_stat_block)

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

    return table

start_table = default_data.sample_character_sheet()
usable_table = dictionary_to_flask_table(start_table)

# Populate the table
table = ItemTable(usable_table)

if __name__ == '__main__':
    app.run(debug=True)