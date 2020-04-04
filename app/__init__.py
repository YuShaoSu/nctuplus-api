import logging
from flask import Flask
from app.model.shared_model import db
from app.configmodule import DevelopmentConfig
from flask_session import Session


def create_app():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s : %(message)s', datefmt='%m-%d %H:%M')
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig())
    sess = Session(app)

    with app.app_context():
        db.init_app(app)
        sess.init_app(app)
        db.create_all(app=app)
        sess.app.session_interface.db.create_all()

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app
