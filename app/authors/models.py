from app.extensions.database import db, CRUDMixin
from datetime import datetime

class Author(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))