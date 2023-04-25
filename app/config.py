from os import environ
from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL')

ARTICLES_PER_PAGE = 2
AUTHORS_PER_PAGE = 2