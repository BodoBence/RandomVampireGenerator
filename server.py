from flask import Flask, render_template, request
from random_vampire_genreator import generate
#from default_data import basic_info_request_data
from default_data import basic_info_request_web_data, default_clans_data, default_weights_data

app = Flask(__name__)

@app.route('/', )
def home():
    # for getting input from script
    #default_inputs = basic_info_request_data()

    # for getting input from user
    default_inputs = basic_info_request_web_data()
    clan_inputs = default_clans_data()
    weight_inputs = default_weights_data() 
    return render_template('basic_info_request.html',
                           requested_non_slider_data = default_inputs,
                           requested_clan_data = clan_inputs,
                           requested_slider_data = weight_inputs)

@app.route('/result', methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template('vampire_result.html', result = result)    

@app.route('/<name>')
def user(name):
    return f'hello {name}, i vuv ya!'

@app.route('/generator')
def generator():
    char_sheet = generate()
    return char_sheet

if __name__ == '__main__':
    app.run(debug=True)
    