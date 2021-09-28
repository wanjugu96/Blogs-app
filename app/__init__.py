from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import  config_options
from flask_uploads import UploadSet,configure_uploads,IMAGES
bootstrap=Bootstrap()
db=SQLAlchemy()
login_manager=LoginManager()
login_manager.session_protection='strong'
login_manager.login_view='auth.login'

photos=UploadSet('photos',IMAGES)


def create_app(config_name):
    app= Flask(__name__)

    #creating app configurations
    app.config.from_object(config_options[config_name])

    #initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    configure_uploads(app,photos)


   

    #register Blueprint
    from .main import main as main_Blueprint
    app.register_blueprint(main_Blueprint)

    from .auth import auth as auth_Blueprint
    app.register_blueprint(auth_Blueprint,url_prefix='/authenticate')

    


    return app