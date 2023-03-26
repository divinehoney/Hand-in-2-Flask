from flask import Flask, render_template, url_for, send_file
from . import articles, simple_pages
from app.extensions.database import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')
    
    register_extensions(app)
    register_blueprints(app)

    return app

# Blueprints
def register_blueprints(app: Flask):
    app.register_blueprint(articles.routes.blueprint)
    app.register_blueprint(simple_pages.routes.blueprint)

def register_extensions(app: Flask):
    db.init_app(app)
# initializes the database connection of SQLAlchemy and passes the app (which is our Flask application object) as an argument