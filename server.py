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
    starting_field_deails = server_functions.start_field_values()

    return render_template('basic_info_request.html',
                           requested_non_slider_data = default_inputs,
                           requested_slider_data = weight_inputs,
                           detail = starting_field_deails)

@app.route('/result', methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        weight_inputs = default_data.default_weights_data()
            
        result = request.form

        starting_field_details =  server_functions.input_form_to_field(result)
        input_values, weight_values = server_functions.input_form_to_generator(result)
 
        #character_df.to_csv('character.csv', sep='\t')
        start_table = generate(input_values, weight_values)
        usable_table = server_functions.dictionary_to_flask_table(start_table)
        converted_to_flask_table = ItemTable(usable_table)
        return render_template("basic_info_request.html",
                                   requested_slider_data = weight_inputs,
                                   detail = starting_field_details,
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
    