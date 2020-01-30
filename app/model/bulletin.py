from .shared_model import db


class Bulletin(db.Model):
    title = db.Column(db.String(1000), nullable=False)
    category = db.Column(db.Integer)
    author_id = db.Column(db.BigInteger, nullable=False)
    begin_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
