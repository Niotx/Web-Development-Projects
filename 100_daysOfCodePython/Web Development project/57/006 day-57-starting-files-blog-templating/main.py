from flask import Flask, render_template,url_for
import requests

app = Flask(__name__)

@app.route('/')
def home():
    URL = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(URL)
    responseData = response.json()
    return render_template("index.html", posts=responseData)

@app.route('/blog/<int:blog_id>')
def get_blog(blog_id):
    URL = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(URL)
    responseData = response.json()
    return render_template('post.html', posts=responseData, id=blog_id - 1)

if __name__ == "__main__":
    app.run(debug=True)
