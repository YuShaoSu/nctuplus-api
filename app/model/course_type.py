from .shared_model import db
from sqlalchemy import text


class CourseType(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type_name = db.Column(db.String(20), nullable=False, unique=True)
    course = db.relationship('Course', backref='course_type', lazy=True)

    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8mb4'
    }

