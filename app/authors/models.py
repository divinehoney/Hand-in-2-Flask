from app.extensions.database import db, CRUDMixin
from datetime import datetime

class Author(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    date_registered = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    articles = db.relationship('Article', backref='author', lazy=True)