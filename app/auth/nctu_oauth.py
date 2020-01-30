from flask import request, redirect
from app.auth.config import NCTU_OAUTH_URL
from . import auth


@auth.route('/nctu_oauth', methods=['GET'])
def auth_nctu_oauth():
    return redirect(NCTU_OAUTH_URL)

