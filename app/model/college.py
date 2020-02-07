from .shared_model import db
from sqlalchemy import text


class College(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    code = db.Column(db.String(2), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    department = db.relationship('Department', backref='college', lazy=True)

