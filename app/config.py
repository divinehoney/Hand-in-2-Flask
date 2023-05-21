from os import environ
from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL')

ARTICLES_PER_PAGE = 5
AUTHORS_PER_PAGE = 2

SECRET_KEY = environ.get('SECRET_KEY')