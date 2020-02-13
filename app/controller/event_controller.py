from app.model.event import Event
from app.model.event_follower import EventFollower
from app.model.user import User
from app import util
from app.model.shared_model import db
from datetime import datetime

permit_parameter = ['event_type', 'title', 'organization', 'location', 'begin_time', 'end_time', 'content', 'url',
                    'cover_image']


def format_list(func):
    def wrap_function(*args, **kwargs):
        events = func(*args, **kwargs)
        if not events:
            return []
        if isinstance(events, int):
            return events
        events_list = []
        for event in events:
            events_list.append(format_detail(event))
        return events_list

    return wrap_function


def format_(func):
    def wrap_function(*args, **kwargs):
        event = func(*args, **kwargs)
        if not event:
            return None
        if isinstance(event, int):
            return event
        return format_detail(event)

    return wrap_function


def format_detail(e):
    # date format
    e['created_at'] = util.date2str(e['created_at'], True)
    e['updated_at'] = util.date2str(e['updated_at'], True)
    e['begin_time'] = util.date2str(e['begin_time'], False)
    e['end_time'] = util.date2str(e['end_time'], False)
    return e


@format_list
def index():
    return util.obj2list(Event.query.all())


# 'url', 'cover_image' can be null
@format_
def create(data, uid):
    new = Event(uid, data['event_type'], data['title'], data['content'], data['location'], data['organization'],
                data['begin_time'], data['end_time'], data.get('url'), data.get('cover_image'))
    db.session.add(new)
    db.session.commit()
    return util.obj2dict(new)


@format_
def show(eid):
    return util.obj2dict(Event.query.get(eid))


@format_
def update(eid, data, uid):
    event = Event.query.get(eid)

    if event is None:
        return None

    if event.user_id != uid:
        return 403

    for key in data:
        if key not in permit_parameter:
            return 402
        setattr(event, key, data[key])
    event.updated_at = datetime.now()
    db.session.commit()
    return util.obj2dict(event)


def destroy(eid, uid):
    event = Event.query.get(eid)
    if event.user_id != uid:
        return 403
    else:
        db.session.delete(event)
        db.session.commit()
        return 204


def follow(eid, uid):
    event_follow = EventFollower(eid, uid)
    db.session.add(event_follow)
    db.session.commit()
    return 201


def destroy_follow(eid, uid):
    event_follower = EventFollower.query.filter_by(event_id=eid, follower_id=uid).first()
    db.session.delete(event_follower)
    db.session.commit()
    return 204
