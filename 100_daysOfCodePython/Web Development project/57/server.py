from flask import Flask,render_template
import random
import datetime
import requests
import re

app = Flask(__name__)


# https://api.agify.io?name=Tom
# https://api.genderize.io?name=Tom
@app.route('/')
def hello():
    random_number = random.randint(1, 10)
    year = datetime.date.today().year
    return render_template('index.html', num=random_number, year=year)

@app.route('/guess/<name>')
def guess(name):
    agify = {}
    agify = requests.get(f'https://api.agify.io?name={name}')
    genderize = {}
    genderize = requests.get(f'https://api.genderize.io?name={name}')
    return render_template('guess.html', age=agify, gender=genderize)
if __name__ == '__main__':
    app.run(debug=True)