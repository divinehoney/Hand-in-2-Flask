from app.extensions.database import db, CRUDMixin
from datetime import datetime

class Article(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(80))
    title = db.Column(db.String(120))
    reading_time = db.Column(db.String(15))