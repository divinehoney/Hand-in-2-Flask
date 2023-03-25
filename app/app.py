from flask import Flask, render_template, url_for, send_file
from . import articles, simple_pages

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')

    register_blueprints(app)

    return app

# Blueprints
def register_blueprints(app: Flask):
    app.register_blueprint(articles.routes.blueprint)
    app.register_blueprint(simple_pages.routes.blueprint)
