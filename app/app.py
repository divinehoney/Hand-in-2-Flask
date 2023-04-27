from flask import Flask, render_template, url_for, send_file
from . import articles, simple_pages, authors
from app.extensions.database import db, migrate

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
    app.register_blueprint(authors.routes.blueprint)

def register_extensions(app: Flask):
    db.init_app(app)
    # initializes the database connection of SQLAlchemy and passes the app (which is our Flask application object) as an argument
    migrate.init_app(app, db, compare_type=True)
    #the first parameter app tells where to look for the models that are imported in our app
    #the second parameter db tells the script where to find the database that should be dated with the new database tables
    #compare_type is a configuration option; it will enable any changes we make to column types in our models and allow us to create migrations for it