# Imports
from flask import Flask, render_template, request
import uuid

from random_vampire_generator import generate as generate_character
from random_city_generator import generate_random_city as generate_city
import default_data
import server_functions

# Creating flaks appp
app = Flask(__name__)
app.secret_key = unique_key = str(uuid.uuid1())

# Startup variables

# Metadata
VERSION_INFO = '3.01'

# Background values
HAVE_GENERATED_CHARACTER = False
HAVE_GENERATED_CITY = False

# Character Generator defaults
startup_input_field_details = {
    'input_conditions': default_data.start_conditions(),
    'input_values': default_data.start_values(),
    'input_weights': default_data.start_weights(),
    'input_clans': default_data.default_clans_data(),
    'input_generations': default_data.default_generations_data()}

# City Generator defaults
startup_city_input_field_details = {
    'input_values': default_data.start_city_values()}

# Functions for the website pages

# Page Behavior
@app.route('/', )
def home():
    return render_template(
        'main_character_generator.html',
        display_legal = True,
        version = VERSION_INFO,
        field_conditions = startup_input_field_details['input_conditions'],
        field_values = startup_input_field_details['input_values'],
        slider_values = startup_input_field_details['input_weights'],
        default_input_weights=startup_input_field_details['input_weights'],
        clans = startup_input_field_details['input_clans'],
        generations = startup_input_field_details['input_generations'],
        have_generated_character=HAVE_GENERATED_CHARACTER)

@app.route('/result_character', methods = ['POST', 'GET'])
def result_character():
    HAVE_GENERATED_CHARACTER = True

    gathered_input = request.form

    resutrctured_conditions, restructured_values, restructured_weights = server_functions.form_structuring(gathered_input)

    generated_character = generate_character(
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
        'main_character_generator.html',
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

@app.route('/city_generator',  methods = ['POST', 'GET'])
def city_generator():

    return render_template(
        'main_city_generator.html',
        field_values = startup_city_input_field_details['input_values'],
        display_legal = True,
        version = VERSION_INFO,
        default_city_input_values = server_functions.get_default_city_values())

@app.route('/result_city', methods = ['POST', 'GET'])
def result_city():
    HAVE_GENERATED_CITY = True

    generated_city = generate_city(
        faction_ratio_camarilla = int(request.form['slider_camarilla']),
        faction_ratio_sabbath = int(request.form['slider_sabbath']),
        faction_ratio_anarch = int(request.form['slider_anarch']),
        faction_ratio_independent = int(request.form['slider_independent']),
        favor_females = 100 - int(request.form['slider_male_to_female']),
        favor_males = int(request.form['slider_male_to_female']),
        number_of_vampires = int(request.form['slider_n_vampires']),
        age_average = int(request.form['slider_average_age']),
        age_standard_deviation = int(request.form['slider_age_deviation']),
        minimum_sireing_gap = int(request.form['slider_sireing_age_gap'])
    )
    structured_city = server_functions.structure_city(generated_city)

    rendered_city = render_template(
        'main_city_generator.html',
        display_legal = True,
        version = VERSION_INFO,
        field_values = startup_city_input_field_details['input_values'],
        have_generated_city=HAVE_GENERATED_CITY,
        default_city_input_values = server_functions.get_default_city_values(),
        generated_city = structured_city)

    return rendered_city

# Run the app!

if __name__ == '__main__':
    app.run(debug=True)