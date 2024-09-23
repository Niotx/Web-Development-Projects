from flask import Flask, render_template, request, redirect, url_for, make_response
from fpdf import FPDF

app = Flask(__name__)

# Home page (quiz form)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        responses = request.form
        return redirect(url_for('result', **responses))
    return render_template('index.html')

# Result page and PDF generation
@app.route('/result', methods=['GET'])
def result():
    responses = request.args.to_dict()
    pdf = create_pdf(responses)
    response = make_response(pdf.output(dest='S').encode('utf-8'))  # Change encoding to utf-8
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=result.pdf'
    return response


# PDF creation
def create_pdf(responses):
    pdf = FPDF()
    pdf.add_page()
    # Make sure the font path is correct
    pdf.add_font('Vazir', '', 'static/fonts/Vazir.ttf', uni=True)  
    pdf.set_font('Vazir', '', 12)
    pdf.cell(200, 10, txt="نتایج آزمون", ln=True, align="C")
    
    for i, (question, answer) in enumerate(responses.items(), 1):
        pdf.cell(200, 10, txt=f"{i}. {question}: {answer}", ln=True)
    
    return pdf



if __name__ == '__main__':
    app.run(debug=True)
