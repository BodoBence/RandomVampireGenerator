from flask import Flask, render_template, request
from flask_table import Table, Col
from random_vampire_genreator_web import generate
#from default_data import basic_info_request_data
import default_data  
import server_functions
import pprint

app = Flask(__name__)

@app.route('/', )
def home():
    # for getting input from script
    #default_inputs = basic_info_request_data()
    default_inputs = default_data.basic_info_request_web_data()
    clan_inputs = default_data.default_clans_data()
    generation_inputs = default_data.default_generations_data()
    weight_inputs = default_data.default_weights_data()
    starting_field_deails = server_functions.start_field_values()

    return render_template('basic_info_request.html',
                           requested_non_slider_data = default_inputs,
                           requested_clan_data = clan_inputs,
                           requested_generation_data = generation_inputs,
                           requested_slider_data = weight_inputs,
                           detail = starting_field_deails)


@app.route('/result', methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        # for the basic input gather segment    
        default_inputs = default_data.basic_info_request_web_data()
        clan_inputs = default_data.default_clans_data()
        generation_inputs = default_data.default_generations_data()
        weight_inputs = default_data.default_weights_data()
            
        # for the character generation based on the gatehred values
        result = request.form

        starting_field_details =  server_functions.input_form_to_field(result)
        input_values, weight_values = server_functions.input_form_to_generator(result)
 
        #character_df.to_csv('character.csv', sep='\t')
        start_table = generate(input_values, weight_values)
        usable_table = server_functions.dictionary_to_flask_table(start_table)
        converted_to_flask_table = ItemTable(usable_table)
        #return render_template('vampire_result.html', generated_character=character)
        return render_template("basic_info_request.html",
                                   requested_non_slider_data = default_inputs,
                                   requested_clan_data = clan_inputs,
                                   requested_generation_data = generation_inputs,
                                   requested_slider_data = weight_inputs,
                                   detail = starting_field_details,
                                   tStrToLoad = converted_to_flask_table.__html__())

# Declare your table
class ItemTable(Table):
    col1 = Col('col1')
    col2 = Col('col2')
    col3 = Col('col3')
    col4 = Col('col4')
    col5 = Col('col5')
    col6 = Col('col6')


if __name__ == '__main__':
    app.run(debug=True)
    