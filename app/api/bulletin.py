from flask import session, request, jsonify
from . import api
from .response import response
from app.model.bulletin import Bulletin
from app.model.shared_model import db
from app.auth.user_handler import get_uid
from app import util

ID = 1
NAME = '王大明'
prefix = 'bulletins'


@api.route('%s' % prefix, methods=['POST'])
def create():
    uid = get_uid()
    if uid is None:
        return response(403, message='not login')
    data = request.form
    new = Bulletin(data['title'], data['category'], uid, data['begin_time'], data['end_time'])
    db.session.add(new)
    db.session.commit()
    new = util.obj2dict(new)
    new['author'] = {
        'user_id': uid,
        'name': NAME
    }
    new.pop('author_id')
    return response(200, response_data=new)


@api.route('%s' % prefix, methods=['GET'])
def index():
    bulletins = util.obj2list(Bulletin.query.all())
    return jsonify(bulletins), 200


@api.route('%s' % prefix, methods=['PATCH'])
def update():
    bid = request.args.get('id')
    data = request.form
