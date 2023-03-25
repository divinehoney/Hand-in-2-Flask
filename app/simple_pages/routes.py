from flask import Blueprint, render_template, send_file

blueprint = Blueprint('simple_pages', __name__)

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

@blueprint.route('/')
def index():
    return render_template('index.html')

@blueprint.route('/about-me/')
def about_me():
    return render_template('about.html', degrees=degrees_data, certificates=certificates_data)

@blueprint.route('/legal')
def legal():
    return send_file('static/downloads/legal.txt', as_attachment=True)