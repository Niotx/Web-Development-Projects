from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1 style="text-align:center">Hello, World!'\
        ' </h1> <p>This is a paragraph.</p>'

@app.route('/<name>/<int:age>')
def bye(name,age):
    return f"you are {name} and you are {age} years old"

if __name__ == "__main__":
    app.run(debug=True)