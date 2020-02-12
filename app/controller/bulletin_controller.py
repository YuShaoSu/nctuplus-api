from app.model.bulletin import Bulletin
from app.model.user import User
from app import util
from app.model.shared_model import db


def author_field_list(func):
    def wrap_function(*args, **kwargs):
        bulletins = func(*args, **kwargs)
        if not bulletins:
            return []

        new_bulletins = []

        for b in bulletins:
            aid = b['author_id']
            author = User.query.get(aid)
            b['author'] = {
                'user_id': aid,
                'name': author.name
            }
            b.pop('author_id')
            new_bulletins.append(b)

        return new_bulletins

    return wrap_function


def author_field(func):
    def wrap_function(*args, **kwargs):
        bulletin = func(*args, **kwargs)
        if not bulletin:
            return None

        aid = bulletin['author_id']
        author = User.query.get(aid)

        bulletin['author'] = {
            'user_id': aid,
            'name': author.name
        }
        bulletin.pop('author_id')

        return bulletin

    return wrap_function


@author_field
def create(data, uid, name):
    new = Bulletin(data['title'], data['category'], uid, data['begin_time'], data['end_time'])
    db.session.add(new)
    db.session.commit()
    return util.obj2dict(new)


@author_field_list
def index():
    return util.obj2list(Bulletin.query.all())


@author_field
def update(bid, data, uid):
    bulletin = Bulletin.query.get(bid)
    if bulletin is None:
        return None

    if bulletin.author_id != uid:
        return 403

    for key in data:
        setattr(bulletin, key, data[key])
    db.session.commit()
    return util.obj2dict(bulletin)


def destroy(bid, uid):
    bulletin = Bulletin.query.get(bid)
    if bulletin.author_id != uid:
        return 403
    else:
        db.session.delete(bulletin)
        db.session.commit()
        return 204
