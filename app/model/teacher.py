from .shared_model import db


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    real_id = db.Column(db.String(10), nullable=False)
    name = db.Column(db.String(10), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8mb4'
    }
