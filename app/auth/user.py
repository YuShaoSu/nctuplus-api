from flask import session, redirect
from . import auth, config


@auth.route('/', methods=['GET'])
def chk_login():
    uid = session.get('uid')
    if uid is None:
        return {'message': 'not login'}, 202
    else:
        return {'uid': uid}, 302


@auth.route('/logout', methods=['GET'])
def logout():
    session['uid'] = False
    return redirect(config.HOME_URL)
