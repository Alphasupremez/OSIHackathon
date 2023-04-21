from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

# define new database
db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    # Initialize app
    app = Flask(__name__)

    # Encrypt/secure cookies & session data related to website
    app.config['SECRET_KEY'] = 'bottle of water' 
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' 

    # Initialize database
    db.init_app(app)

    from .views import my_views
    from .auth import auth

    app.register_blueprint(my_views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note


    return app

"""This function to create a database
    where it checks if there is an existing database"""
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Create Database')



