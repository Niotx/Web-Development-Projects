from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
import json

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///psychtest.db'
app.config['UPLOAD_FOLDER'] = 'uploads'
db = SQLAlchemy(app)

class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    questions = db.Column(db.JSON, nullable=False)
    results_calculation = db.Column(db.JSON, nullable=False)
    timer = db.Column(db.Integer)

class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    test_id = db.Column(db.Integer, db.ForeignKey('test.id'), nullable=False)
    answers = db.Column(db.JSON, nullable=False)
    result = db.Column(db.JSON, nullable=False)

@app.route('/api/tests', methods=['POST'])
def create_test():
    data = request.json
    new_test = Test(
        title=data['title'],
        questions=json.dumps(data['questions']),
        results_calculation=json.dumps(data['resultsCalculation']),
        timer=data.get('timer')
    )
    db.session.add(new_test)
    db.session.commit()
    return jsonify({"message": "Test created successfully", "id": new_test.id}), 201

@app.route('/api/tests', methods=['GET'])
def get_tests():
    tests = Test.query.all()
    return jsonify([{
        "id": test.id,
        "title": test.title,
        "questions": json.loads(test.questions),
        "resultsCalculation": json.loads(test.results_calculation),
        "timer": test.timer
    } for test in tests])

@app.route('/api/tests/<int:test_id>', methods=['GET'])
def get_test(test_id):
    test = Test.query.get_or_404(test_id)
    return jsonify({
        "id": test.id,
        "title": test.title,
        "questions": json.loads(test.questions),
        "resultsCalculation": json.loads(test.results_calculation),
        "timer": test.timer
    })

@app.route('/api/results', methods=['POST'])
def save_result():
    data = request.json
    new_result = Result(
        test_id=data['testId'],
        answers=json.dumps(data['answers']),
        result=json.dumps(data['result'])
    )
    db.session.add(new_result)
    db.session.commit()
    return jsonify({"message": "Result saved successfully", "id": new_result.id}), 201

@app.route('/api/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify({"message": "File uploaded successfully", "filename": filename}), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
