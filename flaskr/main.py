# Imports
from flask import Flask, render_template, request
import uuid
import git

from random_vampire_generator import generate as generate_character
from random_city_generator import generate_random_city as generate_city
import default_data
import server_functions
#Test 4

# Creating flaks appp
app = Flask(__name__)
app.secret_key = unique_key = str(uuid.uuid1())

# Startup variables

# Metadata
VERSION_INFO = '5.0'

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
@app.route('/update_server', methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('/home/autofeed')
        origin = repo.remotes.origin
        # git remote set-url origin https://BodoBence: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@github.com/BodoBence/RandomVampireGenerator.git
        # HTTPS_REMOTE_URL = 'https://<access_token>:x-oauth-basic@github.com/username/your-project' in git config file
        # /var/www/autofeed_pythonanywhere_com_wsgi.py
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400


@app.route('/', methods = ['POST', 'GET'])
def home():
    return render_template(
        'main_character_generator.html',
        display_legal = True,
        version = VERSION_INFO,
        have_generated_character=HAVE_GENERATED_CHARACTER,

        clans = startup_input_field_details['input_clans'],
        generations = startup_input_field_details['input_generations'],

        field_conditions = startup_input_field_details['input_conditions'],
        field_values = startup_input_field_details['input_values'],
        slider_values = startup_input_field_details['input_weights'],
        default_input_weights = startup_input_field_details['input_weights'])

@app.route('/result_character', methods = ['POST', 'GET'])
def result_character():
    HAVE_GENERATED_CHARACTER = True
    gathered_input = request.form
    resutrctured_conditions, restructured_values, restructured_weights = server_functions.form_structuring(gathered_input)
    generated_character = generate_character(
        input_values=restructured_values,
        input_conditions=resutrctured_conditions,
        input_weights=restructured_weights)


    # details = generated_character['Character_Details']
    max_level = server_functions.get_maximum_skill_level(generated_character)
    DISCIPLINES_SKILLS_RITUALS = default_data.get_discipline_skills_and_rituals()
    clan_discipline_dict = default_data.default_clan_disciplines_data()
    clan_list = default_data.default_clans_data()
    generation_based_max_level_dict = default_data.default_generation_based_point_data()

    rendered_vampire = render_template(
        'main_character_generator.html',
        display_legal = True,
        version = VERSION_INFO,
        have_generated_character=HAVE_GENERATED_CHARACTER,

        field_conditions = resutrctured_conditions, # overwrite the input field and slider values
        field_values = restructured_values, # overwrite the input field and slider values
        slider_values = restructured_weights, # overwrite the input field and slider values
        default_input_weights = startup_input_field_details['input_weights'],

        clans = startup_input_field_details['input_clans'],
        predator_types = default_data.get_predator_types(),
        generations = startup_input_field_details['input_generations'],
        DISCIPLINES_SKILLS_RITUALS = DISCIPLINES_SKILLS_RITUALS,
        disciplines_list = default_data.default_disciplines_data(),
        clan_list = clan_list,
        clan_discipline_dict = clan_discipline_dict,
        generation_based_max_level_dict = generation_based_max_level_dict,

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
    # print('------------------------') #DEBUG
    # print('number of vmaps input') #DEBUG
    # print(request.form['slider_n_vampires']) #DEBUG
    generated_city = generate_city(
        n_camarilla = int(request.form['slider_camarilla']),
        n_sabbath = int(request.form['slider_sabbath']),
        n_anarch = int(request.form['slider_anarch']),
        n_independent = int(request.form['slider_independent']),
        favor_females = 100 - int(request.form['slider_male_to_female']),
        favor_males = int(request.form['slider_male_to_female']),
        age_average = int(request.form['slider_average_age']),
        age_standard_deviation = int(request.form['slider_age_deviation'])
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