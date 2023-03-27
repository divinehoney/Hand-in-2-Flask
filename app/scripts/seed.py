from app.app import create_app
from app.articles.models import Article
from app.extensions.database import db

if __name__ == '__main__':
    app = create_app()
    app.app_context().push()

articles_data = {
    'moscow': {'name': 'Racism in Russia', 'reading_time': '7 mins'},
    'german': {'name': 'How to Learn German', 'reading_time': '4 mins'},
    'mtg': {'name': 'Magic the Gathering', 'reading_time': '15 mins'},
    'berlin': {'name': 'Tipps on Finding a Flat in Berlin', 'reading_time': '10 mins'},
    'empathy': {'name': 'Key to a Happy Relationship', 'reading_time': '8 mins'},
    'habit': {'name': 'Review of Some Habit Tracking Apps', 'reading_time': '7 mins'},
}

for slug, article in articles_data.items():
    new_article = Article(slug=slug, title=article['name'], reading_time = article['reading time'])

db.session.commit()