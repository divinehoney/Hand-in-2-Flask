from flask import Blueprint, render_template, request, current_app, redirect, url_for
from .models import Article
from .services.create_article import create_article
from .services.delete_article import delete_article

blueprint = Blueprint('articles', __name__)

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
    
@blueprint.route('/deletearticle', methods=["POST", "GET"])
def delete_article_by_user():
    all_articles = Article.query.all()
    if request.method == "POST":
        delete_article(request.form)
        return redirect(url_for('articles.delete_article_by_user'))


    return render_template('articles/delete.html', html_articles = all_articles)