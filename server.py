from flask import Flask, render_template, request
from random_vampire_genreator import generate
#from default_data import basic_info_request_data
from default_data import basic_info_request_data_lists

app = Flask(__name__)

@app.route('/')
def home():
    #default_inputs = basic_info_request_data()
    default_inputs = basic_info_request_data_lists()
    return render_template('basic_info_request.html',  requested_data = default_inputs)

@app.route('/result',methods = ['POST', 'GET'])
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
    