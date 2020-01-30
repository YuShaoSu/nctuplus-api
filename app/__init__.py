import logging
from flask import Flask
from app.model.shared_model import db


def create_app():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s : %(message)s', datefmt='%m-%d %H:%M')
    app = Flask(__name__)

    app.secret_key = '7138a508b1a2ade2faea975e'
    app.config['JSON_AS_ASCII'] = False
    app.debug = True
    # app.env = 'production'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://yussu016_cs:dbliang@dbhome.cs.nctu.edu.tw' \
                                            '/yussu016_cs_nctuplus_development'
    app.config['SQLALCHEMY_ECHO'] = True
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS']

    db.init_app(app)
    with app.app_context():
        db.create_all()

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app
