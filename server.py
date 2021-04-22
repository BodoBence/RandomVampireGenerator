from flask import Flask
from random_vampire_genreator import generate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'wawu'

@app.route('/')
def home():
    return 'Welcome to the <h1>BODO-ZSOLYOMI VAMPCHARGEN 2021 ALL RIGHTS RESERVED<h1>'

@app.route('/<name>')
def user(name):
    return f'hello {name}, i vuv ya!'

@app.route('/generator')
def generator():
    char_sheet = generate()
    return char_sheet

if __name__ == '__main__':
    app.run()
    