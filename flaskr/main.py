# Imports
from flask import Flask, render_template, request
import pprint
import uuid
import os
import json

from random_vampire_generator import generate
import default_data  
import server_functions


# Creating flaks appp
app = Flask(__name__)
app.secret_key = unique_key = str(uuid.uuid1())


# Startup variables

startup_input_field_details = {
    'input_conditions': default_data.start_conditions(),
    'input_values': default_data.start_values(),
    'input_weights': default_data.start_weights()}

HAVE_GENERATED_CHARACTER = False
SCRIPT_DIR = os.path.dirname(__file__)
CHARACTER_INDEX = os.path.join(SCRIPT_DIR, 'character_index.json')
STORED_CHARACTERS_DIR = os.path.join(SCRIPT_DIR, 'generated_characters')
MAX_STORED_CHARACTERS = 4

# Functions for the website pages

@app.route('/', )
def home():
    return render_template(
        'home.html',
        field_conditions = startup_input_field_details['input_conditions'],
        field_values = startup_input_field_details['input_values'],
        slider_values = startup_input_field_details['input_weights'],
        default_input_weights=startup_input_field_details['input_weights'],
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

    store_generated_character(generated_character)

    # overwrite the input field and slider valies
    startup_input_field_details['input_conditions'] = resutrctured_conditions
    startup_input_field_details['input_values'] = restructured_values
    startup_input_field_details['input_weights'] = restructured_weights

    details = generated_character['Character_Details']
    attributes, skills, disciplines, max_level = server_functions.dictionary_to_html_table(generated_character)

    rendered_vampire = render_template(
        'home.html',
        field_conditions = resutrctured_conditions,
        field_values = restructured_values,
        slider_values = restructured_weights,
        default_input_weights=startup_input_field_details['input_weights'],
        have_generated_character=HAVE_GENERATED_CHARACTER,
        details = details, 
        attributes = attributes, 
        skills = skills, 
        disciplines = disciplines,
        max_level = max_level,
        pdf_path = 'output_path')


    return rendered_vampire

@app.route('/contact', )
def contact():
    return render_template('contact.html')

@app.route('/development_road', )
def development_road():
    return render_template('development_road.html')

@app.route('/calculation_maths', )
def calculation_maths():
    return render_template('calculation_maths.html')

@app.route('/encounter_tracker',  methods = ['POST', 'GET'])
def encounter_tracker():
    return render_template('encounter_tracker.html')


@app.route('/collection_start', methods = ['POST', 'GET'])
def collection_start():
    with open(CHARACTER_INDEX) as index:
        current_characters = json.load(index)

    return render_template('collection.html',
        characters = current_characters,
        have_generated_character=False)

@app.route('/collection_chosen', methods = ['POST', 'GET'])
def collection_chosen():
    selected_character = request.form
    print(selected_character)

    with open(CHARACTER_INDEX) as index:
        current_characters = json.load(index)

    stored_character_path = os.path.join(
        STORED_CHARACTERS_DIR, 
        selected_character['generated_characters'])

    with open(stored_character_path) as character:
        character_to_display = json.load(character)

    print(stored_character_path)
    print("hi")
    print(selected_character)
    
    details = character_to_display['Character_Details']
    attributes, skills, disciplines, max_level = server_functions.dictionary_to_html_table(character_to_display)

    return render_template(
        'collection.html',
        characters = current_characters,
        have_generated_character=True, 
        details = details, 
        attributes = attributes, 
        skills = skills, 
        disciplines = disciplines,
        max_level = max_level)


def store_generated_character(character):
    new_character_file_name = f"{character['Character_Details']['Basic_Information']['Name']}.json"
    new_character_path = os.path.join(SCRIPT_DIR, 'generated_characters', new_character_file_name)

    # write freshly generated character to a json file    
    with open(new_character_path, 'w') as json_file:
        json.dump(character, json_file, indent=4, sort_keys=True)
    
    # Create index for the gerneated chracter's file
    with open(CHARACTER_INDEX) as index:
        if os.stat(CHARACTER_INDEX).st_size == 0:
            current_index = [new_character_file_name]
        else:
            current_index = json.load(index)

            if len(current_index) > MAX_STORED_CHARACTERS:
                removed_character = current_index.pop(0)
                os.remove(os.path.join(STORED_CHARACTERS_DIR, removed_character))

            current_index.append(new_character_file_name)

    # Save the new index file
    with open(CHARACTER_INDEX, 'w') as outf:
        json.dump(current_index, outf, indent=4)


# Run the app!  

if __name__ == '__main__':
    app.run(debug=True)