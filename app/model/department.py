from .shared_model import db
from sqlalchemy import text


class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    department_type = db.Column(db.String(1), nullable=False)
    category = db.Column(db.Integer, nullable=False)
    code = db.Column(db.String(2), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('college.id'), nullable=False)

