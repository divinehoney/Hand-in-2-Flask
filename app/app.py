from . import articles
from flask import Flask, render_template, url_for, send_file

app = Flask(__name__)
app.config.from_object('app.config')

degrees_data = {
    'economics': {'name': 'Bachelor of Economics', 'year of graduation': '2016'},
    'management': {'name': 'Master of IT management', 'year of graduation': '2022'},
    'software': {'name': 'Bachelor of Software Engineering', 'year of graduation': 'nowadays'},
}

certificates_data = {
    'ielts': {'name': 'IELTS', 'comment': '7.5 out of 9.0 (C1)'},
    'testdaf': {'name': 'TestDaF', 'comment': '5445 (B2/C1)'},
    'ux': {'name': 'User Experience for Web Design', 'comment': 'from LinkedIn Learning'},
}

app.register_blueprint(articles.routes.blueprint)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about-me/')
def about_me():
    return render_template('about.html', degrees=degrees_data, certificates=certificates_data)

@app.route('/legal')
def legal():
    return send_file('static/downloads/legal.txt', as_attachment=True)