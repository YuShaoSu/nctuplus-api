from flask import session, redirect
from . import auth, config


@auth.route('/', method=['GET'])
def chk_login():
    uid = session.get('uid')
    if uid is None:
        return {'message': 'not login'}, 202
    else:
        return {'uid': uid}, 302


@auth.route('/logout', method=['GET'])
def logout():
    session['username'] = False
    return redirect(config.HOME_URL)
