from .shared_model import db
from sqlalchemy import text


class PermanentCourse(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    eng_name = db.Column(db.String(200), nullable=False)
    code = db.Column(db.String(10), nullable=False)

    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    department_id = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=False)

    course = db.relationship('Course', backref='permanent_course', lazy=True)

    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8mb4'
    }
