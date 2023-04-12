from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

class CRUDMixin():
    
    def save(self):
        db.session.add(self)
        #adds the model object to the session
        db.session.commit()
        #saves the whole thing to the actual database
        return self
    
    def delete(self):
        db.session.delete(self)
        #removes the object from the database session
        db.session.commit()
        return