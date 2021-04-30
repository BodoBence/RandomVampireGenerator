from flask import Flask, render_template, request
from flask_table import Table, Col
from random_vampire_genreator_web import generate
import default_data  
import server_functions
import pprint

app = Flask(__name__)

@app.route('/', )
def home():
    default_inputs = default_data.basic_info_request_web_data()
    weight_inputs = default_data.default_weights_data()
    starting_field_details = server_functions.start_field_values()

    return render_template('basic_info_request_default.html',
                           requested_non_slider_data = default_inputs,
                           requested_slider_data = weight_inputs,
                           detail = starting_field_details)

@app.route('/result', methods = ['POST', 'GET'])
def result():
    input_field_details = request.form

    # get user input
    input_values, input_weights = server_functions.input_form_to_generator(input_field_details)

    # generate character
    generated_character = generate(input_values, input_weights)

    # format
    generated_character_flask_table_input = server_functions.dictionary_to_flask_table(generated_character)
    converted_to_flask_table = ItemTable(generated_character_flask_table_input) 
    
    return render_template("basic_info_request.html",
                        requested_slider_data = input_weights,
                        detail = input_field_details,
                        genereated_vampire = converted_to_flask_table.__html__())

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
    