from flask import Flask
from flask import render_template, send_from_directory

from html_to_pdf import get_pdf

app = Flask(__name__)

HOST = '0.0.0.0'
PORT = 8080

HTML_EN = 'resume_en.html'
HTML_FR = 'resume_fr.html'

OUTPUT_EN = 'Murad_Mustafayev_CV_en.pdf'
OUTPUT_FR = 'Murad_Mustafayev_CV_fr.pdf'


@app.route('/')
def home():  # put application's code here
    return 'Hello World!'


@app.route('/resume/en/', methods=['GET'])
def resume_en(): return render_template(HTML_EN)


@app.route('/resume/fr/', methods=['GET'])
def resume_fr(): return render_template(HTML_FR)


@app.route('/resume/download/en/', methods=['GET'])
def download_resume_en():
    input_url = f'http://{HOST}:{PORT}/resume/en/'
    get_pdf(input_url, OUTPUT_EN)
    return send_from_directory('../', OUTPUT_EN, as_attachment=True)


@app.route('/resume/download/fr/', methods=['GET'])
def download_resume_fr():
    input_url = f'http://{HOST}:{PORT}/resume/fr/'
    get_pdf(input_url, OUTPUT_FR)
    return send_from_directory('../', OUTPUT_FR, as_attachment=True)


if __name__ == '__main__':
    from waitress import serve

    serve(app, host=HOST, port=PORT)
