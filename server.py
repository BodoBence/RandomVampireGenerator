from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the <h1>BODO-ZSOLYOMI VAMPCHARGEN 2021 ALL RIGHTS RESERVED<h1>'

if __name__ == '__main__':
    app.run()
    