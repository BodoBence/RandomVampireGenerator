from flask import Flask, render_template, request
from flask_table import Table, Col
from random_vampire_genreator_web import generate
import default_data  
import server_functions
import pprint

app = Flask(__name__)

# default_data.default_weights_data() only gives slider names and grouping
# slider values come from: server_functions.start_field_values()
# this way actual values are in a flat dictionary, and slider grouping are represented in a nested dictionary

startup_input_field_details = {'weight_structure': default_data.default_weights_data(),
                               'generator_inputs': server_functions.start_field_values()}

@app.route('/', )
def home():
    return render_template('basic_info_request_default.html',
                           requested_slider_structure = startup_input_field_details['weight_structure'],
                           field_detail = startup_input_field_details['generator_inputs'])

@app.route('/result', methods = ['POST', 'GET'])
def result():
    gathered_input = request.form

    # get user input
    input_values = server_functions.field_value_restucturing(gathered_input)
    input_weights = server_functions.weight_value_restucturing(gathered_input)

    # generate character
    generated_character = generate(input_values, input_weights)

    # overwrite the input field and slider valies
    new_input = server_functions.merge_dictionaries(input_values, 
                                                    server_functions.flatten_dictionary(input_weights))
    startup_input_field_details['generator_inputs'] = new_input

    pprint.pprint(gathered_input)
    pprint.pprint(new_input
    )

    # format
    generated_character_flask_table_input = server_functions.dictionary_to_flask_table(generated_character)
    converted_to_flask_table = ItemTable(generated_character_flask_table_input) 
    
    return startup_input_field_details, render_template("generated_characters.html",
                                                        requested_slider_structure = startup_input_field_details['weight_structure'],
                                                        field_detail = startup_input_field_details['generator_inputs'],
                                                        generated_vampire = converted_to_flask_table.__html__())

# Declare your table
class ItemTable(Table):
    col1 = Col('')
    col2 = Col('')
    col3 = Col('')
    col4 = Col('')
    col5 = Col('')
    col6 = Col('')

if __name__ == '__main__':
    app.run(debug=True)
    