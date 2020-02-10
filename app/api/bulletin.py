from flask import session, request, jsonify
from . import api
from app.model.bulletin import Bulletin
from app.model.shared_model import db
from app import util

ID = 1
NAME = '王大明'
prefix = 'bulletins'


@api.route('%s' % prefix, methods=['POST'])
def create():
    data = request.form
    new = Bulletin(data['title'], data['category'], ID, data['begin_time'], data['end_time'])
    db.session.add(new)
    db.session.commit()
    new = util.obj2dict(new)
    new['author'] = {
        'user_id': ID,
        'name': NAME
    }
    new.pop('author_id')
    return jsonify(new), 200
