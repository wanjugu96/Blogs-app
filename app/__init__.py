from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from config import  config_options

bootstrap=Bootstrap()
db=SQLAlchemy()


def create_app(config_name):
    app= Flask(__name__)

    #initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    

    #creating app configurations
    app.config.from_object(config_options[config_name])

    #register Blueprint
    from .main import main as main_Blueprint
    app.register_blueprint(main_Blueprint)



    return app