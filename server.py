from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'welcome to the home page'

if __name__ == '__name__':
    app.run()
    