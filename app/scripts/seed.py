from app.app import create_app
from app.articles.models import Article
from app.authors.models import Author
from app.extensions.database import db

if __name__ == '__main__':
    app = create_app()
    #create an app instance
    app.app_context().push()
    #initialize an application context; simulates running the application just for the duration the Python script is being executed

articles_data = {
    'moscow': {'name': 'Racism in Russia', 'reading_time': '7 mins'},
    'german': {'name': 'How to Learn German', 'reading_time': '4 mins'},
    'mtg': {'name': 'Magic the Gathering', 'reading_time': '15 mins'},
    'berlin': {'name': 'Tipps on Finding a Flat in Berlin', 'reading_time': '10 mins'},
    'empathy': {'name': 'Key to a Happy Relationship', 'reading_time': '8 mins'},
    'habit': {'name': 'Review of Some Habit Tracking Apps', 'reading_time': '7 mins'},
}

authors_data = {
    'medova': {'first_name': 'Diana', 'last_name': 'Medova'},
    'winter': {'first_name': 'Zhanna', 'last_name': 'Winter'},
}

for slug, article in articles_data.items():
    new_article = Article(slug=slug, title=article['name'], reading_time = article['reading_time'])
    db.session.add(new_article)

db.session.commit()

for slug, author in authors_data.items():
    new_author = Author(first_name=author['first_name'], last_name = author['last_name'])
    db.session.add(new_author)

db.session.commit()