import os

class Config:
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    SQLALCHEMY_DATABASE_URI= 'postgresql+psycopg2://angie:angie12@localhost/pitch'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/Images'


    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(Config):

    SQLALCHEMY_DATABASE_URI = ' postgresql://ilmrqorqveuibb:3ec70886de9fa7ae47a0726803a4a3c28e543d38b03cea91cd02ac6497b8d36d@ec2-3-231-82-226.compute-1.amazonaws.com:5432/d92c1gto56icka'

class DevConfig(Config):

   DEBUG = True
   SQLALCHEMY_DATABASE_URI= 'postgresql+psycopg2://angie:angie12@localhost/pitch'


config_options = {
'development':DevConfig,
'production':ProdConfig,
}