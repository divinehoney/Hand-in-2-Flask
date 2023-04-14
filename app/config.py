from os import environ
import os

os.getenv()
SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL')

ARTICLES_PER_PAGE = 2