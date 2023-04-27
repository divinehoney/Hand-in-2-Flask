from app.articles.models import Article

def create_article(form_data):
    article_to_add = Article(
        title = form_data.get('title'),
        reading_time = form_data.get('reading_time')
    )
    article_to_add.save()