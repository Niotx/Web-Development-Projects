from flask import Flask,render_template,url_for
import random
import datetime
import requests

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
    return render_template('guess.html',persen_name=name, age=agify, gender=genderize)


@app.route('/blog')
def blog():
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template('blog.html', post=all_posts)


if __name__ == '__main__':
    app.run(debug=True)