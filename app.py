from flask import Flask, render_template, url_for, send_file

app = Flask(__name__)
app.config.from_object('config')

articles_data = {
    'moscow': {'name': 'Racism in Russia', 'reading time': '7 mins'},
    'german': {'name': 'How to Learn German', 'reading time': '4 mins'},
    'mtg': {'name': 'Magic the Gathering', 'reading time': '15 mins'},
    'berlin': {'name': 'Tipps on Finding a Flat in Berlin', 'reading time': '10 mins'},
    'empathy': {'name': 'Key to a Happy Relationship', 'reading time': '8 mins'},
    'habit': {'name': 'Review of Some Habit Tracking Apps', 'reading time': '7 mins'},
}

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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about-me/')
def about_me():
    return render_template('about.html', degrees=degrees_data, certificates=certificates_data)

@app.route('/articles/')
def list_of_articles():
    return render_template('articles.html', articles=articles_data)

@app.route('/articles/<slug>')
def each_article(slug):
  return articles_data[slug]

@app.route('/legal')
def legal():
    return send_file('static/downloads/legal.txt', as_attachment=True)

if __name__ == '__main__':
    app.run()