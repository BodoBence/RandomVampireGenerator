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
    
    basic_information_stat_names = []
    basic_information_stat_values = []
    trackers_stat_names = []
    trackers_stat_values = []

    for key, value in character_dictionary['Character_Details']['Basic_Information'].items():
        basic_information_stat_names.append(str(key))
        basic_information_stat_values.append(str(value))

    for key, value in character_dictionary['Character_Details']['Trackers'].items():
        trackers_stat_names.append(str(key))
        trackers_stat_values.append(str(value))

    for x in range(0, (max(len(character_dictionary['Character_Details']['Basic_Information']), len(character_dictionary['Character_Details']['Trackers'])) - 1)):
        row_stat_block = {'col1': basic_information_stat_names[x],
                          'col2': basic_information_stat_values[x],
                          'col3': trackers_stat_names[x] if x < len(trackers_stat_names) else '',
                          'col4': trackers_stat_values[x] if x < len(trackers_stat_values) else '',
                          'col5': "",
                          'col6': ""}
        table.append(row_stat_block)


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