from .shared_model import db
from sqlalchemy import text


class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    department_type = db.Column(db.String(1), nullable=False)
    category = db.Column(db.Integer, nullable=False)
    code = db.Column(db.String(2), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    category_id = db.Column(db.Integer, db.ForeignKey('college.id'), nullable=False)
    permanent_course = db.relationship('PermanentCourse', backref='department', lazy=True)

    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8mb4'
    }
