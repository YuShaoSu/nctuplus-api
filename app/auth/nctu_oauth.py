from flask import request, redirect
from app.auth.config import NCTU_OAUTH_ID, NCTU_OAUTH_SECRET, NCTU_OAUTH_TOKEN, NCTU_OAUTH_URL, NCTU_OAUTH_REDIRECT, \
    NCTU_OAUTH_PROFILE
from . import auth
import requests
import jsons


@auth.route('/nctu_oauth', methods=['GET'])
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

    res_json = requests.post(NCTU_OAUTH_TOKEN, data=post_data).json()
    res = jsons.loads(res_json)
    get_profile(res['access_token'])


def get_profile(access_token):
    access_header = {
        'Authorization': 'Bearer ' + access_token
    }

    res_json = requests.get(NCTU_OAUTH_PROFILE, headers=access_header).json()
    res = jsons.loads(res_json)
    user_handler(res)


def user_handler(res):
    # handle user account, set session, etc.
    print(res)

    return redirect('http://localhost:3000')

