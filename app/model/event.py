from .shared_model import db
from sqlalchemy import text


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    event_type = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)
    url = db.Column(db.String(1024), nullable=False)
    cover_image = db.Column(db.String(1024), nullable=False)
    location = db.Column(db.Text, nullable=False)
    organization = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.BigInteger, nullable=False)
    view_count = db.Column(db.Integer, nullable=False, server_default=text('0'))
    follow_count = db.Column(db.Integer, nullable=False, server_default=text('0'))
    begin_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)


    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8mb4'
    }
