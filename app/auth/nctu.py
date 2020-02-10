import logging
from flask import request, redirect, jsonify
from app.auth.config import NCTU_OAUTH_ID, NCTU_OAUTH_SECRET, NCTU_OAUTH_TOKEN, NCTU_OAUTH_URL, NCTU_OAUTH_REDIRECT, \
    NCTU_OAUTH_PROFILE
from . import auth, user_handler
import requests
import app.util as util


@auth.route('/nctu', methods=['GET'])
def auth_nctu_oauth():
    return redirect(NCTU_OAUTH_URL)


@auth.route('/profile', methods=['GET'])
def get_token():
    code = request.args.get('code')

    post_data = {
        'grant_type': 'authorization_code',
        'code': code,
        'client_id': NCTU_OAUTH_ID,
        'client_secret': NCTU_OAUTH_SECRET,
        'redirect_uri': NCTU_OAUTH_REDIRECT
    }

    res = requests.post(NCTU_OAUTH_TOKEN, data=post_data).json()
    get_profile(res['access_token'])


def get_profile(access_token):
    access_header = {
        'Authorization': 'Bearer ' + access_token
    }
    # {'username': '0516016', 'email': 'neighborbob.cs05@nctu.edu.tw'}
    res = requests.get(NCTU_OAUTH_PROFILE, headers=access_header).json()
    user = util.obj2dict(user_handler.get_nctu_user(res))
    print(user)
    return jsonify(user)

    # create or exists
    # user_handler(res)
    # set cookie, response, redirect...
