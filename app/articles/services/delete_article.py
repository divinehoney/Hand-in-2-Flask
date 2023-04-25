from app.articles.models import Article

def delete_article(form_data):
    title = form_data.get('articles')
    article_to_delete = Article.query.filter_by(title=title).first()
    article_to_delete.delete()