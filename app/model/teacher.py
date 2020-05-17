from .shared_model import db


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    real_id = db.Column(db.String(255), nullable=False, unique=True)
    name = db.Column(db.String(255), nullable=False)

    # created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    # updated_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    course = db.relationship('Course', backref='teacher', lazy=True)


    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8mb4'
    }
