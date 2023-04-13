from flask import Blueprint, render_template, request, current_app
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
    page_number = request.args.get('page', 1, type=int)
    articles_pagination = Article.query.paginate(page=page_number, per_page=current_app.config['ARTICLES_PER_PAGE'])
    return render_template('articles/index.html', html_articles=articles_pagination)

@blueprint.route('/articles/<slug>')
def single_article(slug):
    single_db_article = Article.query.filter_by(slug=slug).first_or_404()
    return render_template('articles/show.html', single_html_article = single_db_article)

@blueprint.get('/articles/postanarticle')
def get_publish_an_article():
    return render_template('articles/new.html')

@blueprint.post('/articles/postanarticle')
def post_publish_an_article():
    return render_template('articles/new.html')