from .shared_model import db
from sqlalchemy import text


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    event_type = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)
    url = db.Column(db.String(1024))
    cover_image = db.Column(db.TEXT)
    location = db.Column(db.Text, nullable=False)
    organization = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.BigInteger, nullable=False)
    view_count = db.Column(db.Integer, nullable=False, server_default=text('0'))
    follow_count = db.Column(db.Integer, nullable=False, server_default=text('0'))
    begin_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    follower = db.relationship('EventFollower', backref='event', lazy=True)

    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8mb4'
    }

    def __init__(self, user_id, event_type, title, content, location, organization, begin_time, end_time, url,
                 cover_image):
        self.user_id = user_id
        self.event_type = event_type
        self.title = title
        self.content = content
        self.location = location
        self.organization = organization
        self.begin_time = begin_time
        self.end_time = end_time
        self.url = url
        self.cover_image = cover_image
