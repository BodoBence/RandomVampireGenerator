# Imports
from flask import Flask, render_template, request
import uuid

from random_vampire_generator import generate
import default_data
import server_functions

# Creating flaks appp
app = Flask(__name__)
app.secret_key = unique_key = str(uuid.uuid1())

# Startup variables

# Metadata
VERSION_INFO = '2.6'

# Generator defaults
startup_input_field_details = {
    'input_conditions': default_data.start_conditions(),
    'input_values': default_data.start_values(),
    'input_weights': default_data.start_weights(),
    'input_clans': default_data.default_clans_data(),
    'input_generations': default_data.default_generations_data()}

# Background values
HAVE_GENERATED_CHARACTER = False

# Functions for the website pages

# Page Behavior
@app.route('/', )
def home():
    return render_template(
        'main_home.html',
        display_legal = True,
        version = VERSION_INFO,
        field_conditions = startup_input_field_details['input_conditions'],
        field_values = startup_input_field_details['input_values'],
        slider_values = startup_input_field_details['input_weights'],
        default_input_weights=startup_input_field_details['input_weights'],
        clans = startup_input_field_details['input_clans'],
        generations = startup_input_field_details['input_generations'],
        have_generated_character=HAVE_GENERATED_CHARACTER)

@app.route('/result', methods = ['POST', 'GET'])
def result():
    HAVE_GENERATED_CHARACTER = True

    gathered_input = request.form

    resutrctured_conditions, restructured_values, restructured_weights = server_functions.form_structuring(gathered_input)

    generated_character = generate(
        input_values=restructured_values,
        input_conditions=resutrctured_conditions,
        input_weights=restructured_weights)


    # overwrite the input field and slider valies
    startup_input_field_details['input_conditions'] = resutrctured_conditions
    startup_input_field_details['input_values'] = restructured_values
    startup_input_field_details['input_weights'] = restructured_weights

    # details = generated_character['Character_Details']
    max_level = server_functions.get_maximum_skill_level(generated_character)

    rendered_vampire = render_template(
        'main_home.html',
        display_legal = True,
        version = VERSION_INFO,
        field_conditions = resutrctured_conditions,
        field_values = restructured_values,
        slider_values = restructured_weights,
        default_input_weights=startup_input_field_details['input_weights'],
        clans = startup_input_field_details['input_clans'],
        generations = startup_input_field_details['input_generations'],
        have_generated_character=HAVE_GENERATED_CHARACTER,
        character = generated_character,
        max_level = max_level)

    return rendered_vampire

@app.route('/about', )
def about():
    return render_template(
        'main_about.html',
        display_legal = False,
        version = VERSION_INFO)

@app.route('/encounter_tracker',  methods = ['POST', 'GET'])
def encounter_tracker():
    return render_template(
        'main_encounter_tracker.html',
        display_legal = True,
        version = VERSION_INFO)

# Run the app!

if __name__ == '__main__':
    app.run(debug=True)