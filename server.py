from flask import Flask, render_template, request
from random_vampire_genreator_web import generate
#from default_data import basic_info_request_data
from default_data import basic_info_request_web_data, default_clans_data, default_weights_data
import pandas as pd

app = Flask(__name__)

@app.route('/', )
def home():
    # for getting input from script
    #default_inputs = basic_info_request_data()

    # for getting input from user
    default_inputs = basic_info_request_web_data()
    clan_inputs = default_clans_data()
    weight_inputs = default_weights_data() 
    return render_template('basic_info_request.html',
                           requested_non_slider_data = default_inputs,
                           requested_clan_data = clan_inputs,
                           requested_slider_data = weight_inputs)

def input_form_results_post_care(gathered_user_input):
    input_values = {'manual_clan_condition': True if 'manual_clan_condition' in gathered_user_input.keys() else False,
                    'manual_generation_condition': True if 'manual_generation_condition' in gathered_user_input.keys() else False,
                    'manual_age_condition': True if 'manual_age_condition' in gathered_user_input.keys() else False,
                    'manual_sex_condition': True if 'manual_sex_condition' in gathered_user_input.keys() else False,
                    'manual_name_condition': True if 'manual_name_condition' in gathered_user_input.keys() else False,
                    'manual_age': int(gathered_user_input['manual_age']),
                    'manual_clan': gathered_user_input['manual_clan'],
                    'manual_sex': gathered_user_input['manual_sex'],
                    'manual_generation': int(gathered_user_input['manual_generation']),
                    'manual_name': gathered_user_input['manual_name']}
   
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

# def convert_to_pandas_df(character_dict):
#     columns = ['main', 'category_type', 'category', 'value']
#     character_df = pd.DataFrame(columns=columns)

#     i = 0
#     for main, main_details in character_dict.items():
#         count_space = 0
#         for category_type, category_details in main_details.items():
#             for category

#         character_df.loc[i,'main'] = main
#     return character_df


@app.route('/result', methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        input_values, weight_values = input_form_results_post_care(result)
        character = generate(input_values, weight_values)

        #character_df = convert_to_pandas_df(character)
        #character_df.to_csv('character.csv', sep='\t')
        
        return render_template('vampire_result.html', generated_character=character)    

if __name__ == '__main__':
    app.run(debug=True)
    