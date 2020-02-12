from flask import request, jsonify
from . import api
from .response import response
from app.model.bulletin import Bulletin
from app.auth.user_handler import get_uid
from app import util
from app.controller import bulletin_controller as bc

ID = 1
NAME = '王大明'
prefix = 'bulletin'


@api.route('%s' % prefix, methods=['POST'])
def create():
    uid = get_uid()
    if uid is None:
        return response(403, message='not login')

    result = bc.create(request.form, uid, NAME)
    return jsonify(result), 200


@api.route('%s' % prefix, methods=['GET'])
def index():
    result = bc.index()
    return jsonify(result), 200


@api.route('%s/<int:bid>' % prefix, methods=['PATCH'])
def update(bid):
    uid = get_uid()
    if uid is None:
        return response(403, message='not login')

    result = bc.update(bid, request.form, uid)
    if result == 403:
        return response(403, message='current user is not the author')
    elif result == 402:
        return response(402, message='patch content error')
    elif result is not None:
        return jsonify(result), 200
    else:
        return {'message': 'PATCH failed'}, 402


@api.route('%s/<int:bid>' % prefix, methods=['DELETE'])
def delete(bid):
    uid = get_uid()
    if uid is None:
        return response(403, message='not login')

    result = bc.destroy(bid, uid)
    if result == 403:
        return response(403, message='current user is not the author')
    else:
        return '', 204
