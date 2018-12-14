from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.mail import Mail
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
from config import config

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    # CORS(app, resources={r"/api/*": {"origins": "*"}})
    app.config.from_object(config[config_name])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    config[config_name].init_app(app)
    # app.secret_key = app.config['SECRET_KEY']

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    #
    # jwt = JWTManager(app)
    # app.config['JWT_BLACKLIST_ENABLED'] = True
    # app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

    # @jwt.token_in_blacklist_loader
    # def check_if_token_in_blacklist(decrypted_token):
    #     jti = decrypted_token['jti']
    #     return RevokedToken.is_jti_blacklisted(jti)
    #
    # from .api import api_blueprint
    # app.register_blueprint(api_blueprint)

    # @app.route('/')
    # def index():
    #     return 'API Dock, a web application for managing and testing your APIs.'

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app