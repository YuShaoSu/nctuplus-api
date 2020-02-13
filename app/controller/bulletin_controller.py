from app.model.bulletin import Bulletin
from app.model.user import User
from app import util
from app.model.shared_model import db
from datetime import datetime

permit_parameter = ['title', 'category', 'begin_time', 'end_time']


def format_list(func):
    def wrap_function(*args, **kwargs):
        bulletins = func(*args, **kwargs)
        if not bulletins:
            return []
        if isinstance(bulletins, int):
            return bulletins

        new_bulletins = []

        for b in bulletins:
            new_bulletins.append(format_detail(b))

        return new_bulletins

    return wrap_function


def format_(func):
    def wrap_function(*args, **kwargs):
        bulletin = func(*args, **kwargs)
        if not bulletin:
            return None
        if isinstance(bulletin, int):
            return bulletin
        return format_detail(bulletin)

    return wrap_function


def format_detail(b):
    # date format
    b['created_at'] = util.date2str(b['created_at'], True)
    b['updated_at'] = util.date2str(b['updated_at'], True)
    if b.get('begin_time') is not None:
        b['begin_time'] = util.date2str(b['begin_time'], False)
    if b.get('end_time') is not None:
        b['end_time'] = util.date2str(b['end_time'], False)
    # author format
    aid = b['author_id']
    author = User.query.get(aid)
    b['author'] = {
        'user_id': aid,
        'name': author.name
    }
    b.pop('author_id')
    return b


@format_list
def index():
    return util.obj2list(Bulletin.query.all())


@format_
def create(data, uid):
    new = Bulletin(data['title'], data['category'], uid, data.get('begin_time'), data.get('end_time'))
    db.session.add(new)
    db.session.commit()
    return util.obj2dict(new)


@format_
def update(bid, data, uid):
    bulletin = Bulletin.query.get(bid)

    if bulletin is None:
        return None

    if bulletin.author_id != uid:
        return 403

    for key in data:
        if key not in permit_parameter:
            return 402
        setattr(bulletin, key, data[key])
    bulletin.updated_at = datetime.now()
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
