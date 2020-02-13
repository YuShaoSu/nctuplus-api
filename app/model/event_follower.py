from .shared_model import db


class EventFollower(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    follower_id = db.Column(db.BigInteger, nullable=False)

    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8mb4'
    }

    def __init__(self, event_id, follower_id):
        self.event_id = event_id
        self.follower_id = follower_id
