def obj2dict(row):
    return dict((col, getattr(row, col)) for col in row.__table__.columns.keys())


def obj2list(rows):
    obj_list = [dict((col, getattr(row, col)) for col in row.__table__.columns.keys()) for row in rows]
    return obj_list
