from flask import Blueprint, render_template
from .models import Article

blueprint = Blueprint('articles', __name__)

articles_data = {
    'moscow': {'name': 'Racism in Russia', 'reading time': '7 mins'},
    'german': {'name': 'How to Learn German', 'reading time': '4 mins'},
    'mtg': {'name': 'Magic the Gathering', 'reading time': '15 mins'},
    'berlin': {'name': 'Tipps on Finding a Flat in Berlin', 'reading time': '10 mins'},
    'empathy': {'name': 'Key to a Happy Relationship', 'reading time': '8 mins'},
    'habit': {'name': 'Review of Some Habit Tracking Apps', 'reading time': '7 mins'},
}

@blueprint.route('/articles/')
def list_of_articles():
    all_articles = Article.query.all()
    return render_template('articles/index.html', articles=all_articles)

@blueprint.route('/articles/<slug>')
def each_article(slug):
  return articles_data[slug]