from .shared_model import db
from sqlalchemy import text

# TODO implementation of time slot conversion and write doc
# 現在 DB 裡用 12bytes(96bit) 的 binary 來保存課程時段
# 16個時段(M~L) * 每週 6 天 = 96 bits
# 所以在傳給前端時我們需要轉換成比較容易讀得懂的形式
# 96bits
# 切成 6 個 2bytes 的 string
# 將每個 2bytes string 轉成長度 16 的 bitmask: [0, 1, 1 ...., 0]
# 將每個 bitmask 轉成時段對應的英文字母陣列: ['A', 'B', 'M']
# 將字母陣列跟 index 結合: [0, ['A, 'B', 'M']]
# 將前面作成的 array 轉成 hash

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # TODO need to define type key-value in doc
    course_type = db.Column(db.Integer)
    credit = db.Column(db.Integer)
    hour = db.Column(db.Integer)
    code = db.Column(db.Integer, nullable=False)
    classroom = db.Column(db.String(10))
    grade = db.Column(db.Integer)
    semester = db.Column(db.String(10), nullable=False)
    ext = db.Column(db.String(200), nullable=False)
    memo = db.Column(db.String(200), nullable=False)
    registration_count = db.Column(db.Integer)
    registration_limit = db.Column(db.Integer)
    time_slot = db.Column(db.LargeBinary)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    permanent_course_id = db.Column(db.Integer, db.ForeignKey('permanent_course.id'), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'), nullable=False)

    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8mb4'
    }
