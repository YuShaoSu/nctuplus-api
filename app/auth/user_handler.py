import logging
from flask import session
from app.model.user import User
from app.model.shared_model import db


# 0 for nctu, 1 for facebook
def get_nctu_user(profile):
    user = User.query.filter_by(student_id=profile['username']).first()

    if user is None:
        logging.info('[NCTU OAUTH] create new user %s' % profile['username'])
        new_user = User(student_id=profile['username'], nctu=True, facebook_id=None, facebook=False, name='王大明',
                        email=profile['email'], admission_year=109, provider='nctu')
        db.session.add(new_user)
        db.session.commit()
        set_session(new_user)
        return new_user
    else:
        logging.info('[NCTU OAUTH] user exists %s' % profile['username'])
        set_session(user)
        return user


def set_session(user):
    session['uid'] = user.id
