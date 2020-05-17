from .shared_model import db
from sqlalchemy import text


class CourseExt(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ext = db.Column(db.String(20), nullable=False, unique=True)
    course = db.relationship('Course', backref='course_ext', lazy=True)

    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8mb4'
    }

