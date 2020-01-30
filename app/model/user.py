from .shared_model import db
from sqlalchemy import text


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.String(8), uniqle=False, nullable=False)
    name = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(321), nullable=False)
    admission_year = db.Column(db.Integer)
    role = db.Column(db.Integer, server_default=text('0'))
    provider = db.Column(db.String(321), nullable=False)  # for what?
    encrypted_password = db.Column(db.String(256), nullable=False)
    reset_password_token = db.Column(db.String(256))
    reset_password_sent_at = db.Column(db.DateTime)
    allow_password_change = db.Column(db.Boolean, nullable=False, server_default=text('True'))
    sign_in_count = db.Column(db.Integer, nullable=False, server_default=text('0'))
    current_sign_in_at = db.Column(db.DateTime)
    last_sign_in_at = db.Column(db.DateTime)
    current_sign_in_ip = db.Column(db.String(16))
    last_sign_in_ip = db.Column(db.String(16))
    confirmation_token = db.Column(db.String(256))
    confirmed_at = db.Column(db.DateTime)
    confirmation_sent_at = db.Column(db.DateTime)
    unconfirmed_email = db.Column(db.String(321))
    agree_to_term_of_service = db.Column(db.Boolean, nullable=False, server_default=text('True'))
    agree_to_share_course_table = db.Column(db.Boolean, nullable=False, server_default=text('True'))
    tokens = db.Column(db.Text)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
