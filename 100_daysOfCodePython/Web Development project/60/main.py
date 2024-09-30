from flask import Flask,render_template,request


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def recive_data():
    UN = request.form['username']
    PS = request.form['password']
    if request.method == 'POST':
        return render_template('login.html', user=UN, pasw=PS) 
    else:
        error = 'Invalid username/password'

if __name__ == '__main__':
    app.run(debug=True)