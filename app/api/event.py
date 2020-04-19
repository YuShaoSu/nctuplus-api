from flask import request, jsonify
from . import api
from .response import response
from app.auth.user_handler import get_uid
from app.controller import event_controller as ec

ID = 1
NAME = '王大明'
prefix = 'event'


@api.route('%s' % prefix, methods=['POST'])
def create_event():
    # uid = get_uid()
    # if uid is None:
    #     return response(403, message='not login')

    result = ec.create(request.form, get_uid())
    return jsonify(result), 200


@api.route('%s' % prefix, methods=['GET'])
def index_event():
    result = ec.index()
    return jsonify(result), 200


@api.route('%s/<int:eid>' % prefix, methods=['GET'])
def show_event(eid):
    result = ec.show(eid)
    return jsonify(result), 200


@api.route('%s/<int:eid>' % prefix, methods=['PATCH'])
def update_event(eid):
    # uid = get_uid()
    # if uid is None:
    #     return response(403, message='not login')

    result = ec.update(eid, request.form, get_uid())
    if result == 403:
        return response(403, message='current user is not the author')
    elif result == 402:
        return response(402, message='patch content error')
    elif result is not None:
        return jsonify(result), 200
    else:
        return {'message': 'PATCH failed'}, 402


@api.route('%s/<int:eid>' % prefix, methods=['DELETE'])
def delete_event(eid):
    # uid = get_uid()
    # if uid is None:
    #     return response(403, message='not login')

    result = ec.destroy(eid, get_uid())
    if result == 403:
        return response(403, message='current user is not the author')
    else:
        return '', 204


@api.route('%s/<int:eid>/follow' % prefix, methods=['POST'])
def follow_event(eid):
    # uid = get_uid()
    # if uid is None:
    #     return response(403, message='not login')
    return '', ec.follow(eid, get_uid())


@api.route('%s/<int:eid>/follow' % prefix, methods=['DELETE'])
def delete_follow_event(eid):
    # uid = get_uid()
    # if uid is None:
    #     return response(403, message='not login')
    return '', ec.destroy_follow(eid, get_uid())
