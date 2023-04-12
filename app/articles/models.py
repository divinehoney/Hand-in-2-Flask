from app.extensions.database import db, CRUDMixin
from datetime import datetime

class Article(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(80), unique=True)
    title = db.Column(db.String(120))
    text = db.Column(db.Text())
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    date_published = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    reading_time = db.Column(db.String(15))