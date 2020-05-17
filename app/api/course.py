from flask import request, jsonify
from . import api
from .response import response
from app.auth.user_handler import get_uid


prefix = 'course'

@api.route('%s' % prefix, methods=['POST'])
def all_course():
    pass
