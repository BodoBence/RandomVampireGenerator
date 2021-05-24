# Imports
from flask import Flask, render_template, request
import pprint
import sqlite3
import uuid
import os

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

    pprint.pprint(gathered_input)

    resutrctured_conditions, restructured_values, restructured_weights = server_functions.form_structuring(gathered_input)
    generated_character = generate(
        input_values=restructured_values,
        input_conditions=resutrctured_conditions,
        input_weights=restructured_weights)

    # overwrite the input field and slider valies
    startup_input_field_details['input_conditions'] = resutrctured_conditions
    startup_input_field_details['input_values'] = restructured_values
    startup_input_field_details['input_weights'] = restructured_weights

    details = generated_character['Character_Details']
    attributes, skills, disciplines, max_level = server_functions.dictionary_to_html_table(generated_character)

    store_generated_character(details, attributes, skills, disciplines, max_level)

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


@app.route('/collection', methods = ['POST', 'GET'])
def collection():
    return render_template('collection.html',
        have_generated_character=HAVE_GENERATED_CHARACTER,)


def store_generated_character(details, attributes, skills, disciplines, max_level):
    # unique_key = str(uuid.uuid1())
    pass

# Database functions

def data_base_check(input_file_path):
    if os.path.isfile(input_file_path):
        return True
    else:
        return False


def create_db():
    conn = sqlite3.connect(DB_PATH)
    print("Opened database successfully")

    conn.execute('CREATE TABLE vampires (name TEXT, data1 TEXT)')
    print("Table created successfully")
    conn.close()


def add_to_db(target_db, name_to_add, data1_to_add):
    with sqlite3.connect(target_db) as con:
        cur = con.cursor()
        cur.execute("INSERT INTO vampires (name, data1) VALUES (?,?)", (name_to_add, data1_to_add))
        con.commit()
    

# Actual databse cration and handling

SCRIPT_DIR = os.path.dirname(__file__)
DB_PATH = os.path.join(SCRIPT_DIR, 'database.db')

if data_base_check(DB_PATH) == False:
    create_db()
    pass

if data_base_check(DB_PATH) == True:
    add_to_db(DB_PATH, 'vampire 2', 'is not hungry')

# Run the app!  

if __name__ == '__main__':
    app.run(debug=True)