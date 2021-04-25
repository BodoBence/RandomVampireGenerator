# import things
from flask import Flask, render_template
from flask_table import Table, Col
import default_data

app = Flask(__name__)

@app.route('/', )
def home():
    return table.__html__()

    
# Declare your table
class ItemTable(Table):
    col1 = Col('col1')
    col2 = Col('col2')
    col3 = Col('col3')
    col4 = Col('col4')
    col5 = Col('col5')
    col6 = Col('col6')

def dictionary_to_flask_table(character_dictionary):
    table = []
    # category separator rows
    for categoreies_keys, categories_values in character_dictionary.items():
        row = {'col1': categoreies_keys,
               'col2': "Nothing",
               'col3': "Nothing",
               'col4': "Nothing",
               'col5': "Nothing",
               'col6': "Nothing"}
        table.append(row)
        for types_keys, types_values in categories_values.items():
            row = {'col1': types_keys,
                   'col2': "Nothing",
                   'col3': "Nothing",
                   'col4': "Nothing",
                   'col5': "Nothing",
                   'col6': "Nothing"}
            table.append(row)
            for stats_keys, stats_values in types_values.items():
                row = {'col1': stats_keys,
                       'col2': stats_values,
                       'col3': "Nothing",
                       'col4': "Nothing",
                       'col5': "Nothing",
                       'col6': "Nothing"}
                table.append(row)
    return table

start_table = default_data.sample_character_sheet()
usable_table = dictionary_to_flask_table(start_table)

# Populate the table
table = ItemTable(usable_table)

if __name__ == '__main__':
    app.run(debug=True)