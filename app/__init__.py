from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail
from flask_simplemde import SimpleMDE



login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

mail = Mail()
simple = SimpleMDE()

bootstrap = Bootstrap()
db = SQLAlchemy()

photos = UploadSet('photos',IMAGES)

def create_app(config_name):

    app = Flask(__name__)

   
    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    app.config["SQLALCHEMY_DATABASE_URI"] = ' postgresql://ilmrqorqveuibb:3ec70886de9fa7ae47a0726803a4a3c28e543d38b03cea91cd02ac6497b8d36d@ec2-3-231-82-226.compute-1.amazonaws.com:5432/d92c1gto56icka'
    app.config['SECRET_KEY']='123456789'

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    simple.init_app(app)


     # configure UploadSet
    configure_uploads(app,photos)


    # Registering the blueprint
    # from
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')


    # setting config
    # from .request import configure_request
    # configure_request(app)

    return app








