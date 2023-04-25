from flask import Blueprint, render_template, request, current_app
from .models import Article
from .services.create_article import create_article

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

@blueprint.get('/publisharticle')
def get_publish_an_article():
    return render_template('articles/new.html')

@blueprint.post('/publisharticle')
def post_publish_an_article():
    try:
        if not all([
            request.form.get('title'),
            request.form.get('reading_time'),
            request.form.get('content')
        ]):
            raise Exception('Please fill out all article fields.')
    
        create_article(request.form)
        return render_template('articles/new.html')
    
    except Exception as error_message:
        error = error_message or 'An error occured while processing your article. Please make sure to enter valid data.'

        current_app.logger.info(f'Error creating an article: {error}')

        return render_template('articles/new.html', error = error)
    
@blueprint.get('/deletearticle')
def get_delete_article():
    all_articles = Article.query.all()
    return render_template('articles/delete.html', html_articles = all_articles)