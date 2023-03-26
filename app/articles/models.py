from app.extensions.database import db

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(80), unique=True)
    name = db.Column(db.String(80))
    date_published = db.Column(db.Date)
    reading_time = db.Column(db.String(15))