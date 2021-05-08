from flask import Flask, render_template, request, url_for
from flask_table import Table, Col
from random_vampire_genreator_web import generate
import default_data  
import server_functions
import pprint

app = Flask(__name__)

# default_data.default_weights_data() only gives slider names and grouping
# slider values come from: server_functions.start_field_values()
# this way actual values are in a flat dictionary, and slider grouping are represented in a nested dictionary

startup_input_field_details = {'weight_structure': default_data.default_weights_structure(),
                               'input_conditions': default_data.start_conditions(),
                               'input_values': default_data.start_values(),
                               'input_weights': default_data.start_weights()}


@app.route('/', )
def home():
    return render_template('basic_info_request_default.html',
                           slider_structure = startup_input_field_details['weight_structure'],
                           field_conditions = startup_input_field_details['input_conditions'],
                           field_values = startup_input_field_details['input_values'],
                           slider_values = startup_input_field_details['input_weights'])


@app.route('/result', methods = ['POST', 'GET'])
def result():
    gathered_input = request.form

    # pprint.pprint(gathered_input)

    resutrctured_conditions, restructured_values, restructured_weights = server_functions.form_structuring(gathered_input)

    generated_character = generate(input_values=restructured_values,
                                   input_conditions=resutrctured_conditions,
                                   input_weights=restructured_weights)

    # overwrite the input field and slider valies
    startup_input_field_details['input_conditions'] = resutrctured_conditions
    startup_input_field_details['input_values'] = restructured_values
    startup_input_field_details['input_weights'] = restructured_weights

    # pprint.pprint(gathered_input)
    # pprint.pprint(new_input)

    # format
    #generated_character_flask_table_input = server_functions.dictionary_to_flask_table(generated_character)
    #converted_to_flask_table = ItemTable(generated_character_flask_table_input)
    #pprint.pprint(generated_character_flask_table_input)

    details, attributes, skills, disciplines, max_level = server_functions.dictionary_to_html_table(generated_character)
    

    return render_template("generated_characters_designed.html",
                           slider_structure = startup_input_field_details['weight_structure'],
                           field_conditions = startup_input_field_details['input_conditions'],
                           field_values = startup_input_field_details['input_values'],
                           slider_values = startup_input_field_details['input_weights'],
                           #generated_character = converted_to_flask_table.__html__())
                           details = details, 
                           attributes = attributes, 
                           skills = skills, 
                           disciplines = disciplines,
                           max_level = max_level)

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
    