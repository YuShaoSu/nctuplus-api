from .shared_model import db


class Bulletin(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(1000), nullable=False)
    category = db.Column(db.Integer)
    author_id = db.Column(db.BigInteger, nullable=False)
    begin_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8mb4'
    }

    def __init__(self, title, category, author_id, begin_time, end_time):
        self.title = title
        self.category = category
        self.author_id = author_id
        self.begin_time = begin_time
        self.end_time = end_time
