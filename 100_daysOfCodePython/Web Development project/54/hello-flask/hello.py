from flask import Flask


def make_bold(func):
    def wraper(*args, **kwargs):
        return "<b>" + func() + "</b>"
    return wraper

def make_emphasis(func):
    def wraper():
        return "<em>" + func() + "<em>"
    return wraper

def make_underlined(func):
    def wraper():
        return "<u>" + func() + "</u>"
    return wraper

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1 style="text-align:center">Hello, World!'\
        ' </h1> <p>This is a paragraph.</p>'

@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def decorator_t():
    return "bye"



# @app.route('/<name>/<int:age>')
# def bye(name,age):
#     return f"you are {name} and you are {age} years old"

if __name__ == "__main__":
    app.run(debug=True)