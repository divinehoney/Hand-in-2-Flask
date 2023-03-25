from . import articles, simple_pages
from flask import Flask, render_template, url_for, send_file

app = Flask(__name__)
app.config.from_object('app.config')

app.register_blueprint(articles.routes.blueprint)
app.register_blueprint(simple_pages.routes.blueprint)