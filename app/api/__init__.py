from flask import Blueprint

api = Blueprint('api', __name__)


@api.before_request
def user_auth():
    print('blueprint before_request')
    # if uid is None:
    #     return response(403, message='not login')


from . import bulletin, event
