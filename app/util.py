def obj2dict(row):
    return dict((col, getattr(row, col)) for col in row.__table__.columns.keys())
