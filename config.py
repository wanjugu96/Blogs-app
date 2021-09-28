import os 
from re import DEBUG

class Config:
    DEBUG=True
    TEMPLATES_AUTO_RELOAD = True
    QUOTES_API_BASE_URL='cccc'
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://postgres:Serum2551@localhost/blogpost'
    SECRET_KEY = os.environ.get('SECRET_KEY')    
    UPLOADED_PHOTOS_DEST='app/static/photos'

class ProdCofig(Config):
    pass

class DevConfig(Config):
    DEBUG=True

config_options={
    'development':DevConfig,
    'production':ProdCofig
}

