from .shared_model import db
from sqlalchemy import text


class Slogan(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(1000), nullable=False)
    display = db.Column(db.Boolean, server_default=text('True'))
    author_id = db.Column(db.BigInteger, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

