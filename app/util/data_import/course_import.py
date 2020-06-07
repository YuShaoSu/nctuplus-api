import json
import sys
import urllib.request
import re
from config import course_url

with urllib.request.urlopen(course_url + "?acy=" + sys.argv[1] + "&sem=" + sys.argv[2]) as url:
    raw_courses = json.loads(url.read().decode())

# with open('../../model/seed/course.json') as f:
#     raw_courses = json.load(f)

alpha2num = {
    'N': 0,
    'M': 1,
    'A': 2,
    'B': 3,
    'C': 4,
    'D': 5,
    'X': 6,
    'E': 7,
    'F': 8,
    'G': 9,
    'H': 10,
    'Y': 11,
    'I': 12,
    'J': 13,
    'K': 15,
    'L': 16
}
pattern_day = '([0-9][A-Z]+)'
pattern_slot = '[A-Z]'

# first update cos_type, cos_typeext, building and classroom?, time_slot
#

def forien_key_chk(unique_list, column, c):
    if c[column] not in unique_list:
        unique_list.append(c[column])


def timeslot_convert(t):
    byte_slot = 0
    for d in re.findall(pattern_day, t):
        weekday = int(d[0])
        for s in re.findall(pattern_slot, d):
            # make byte
            byte_slot += (1 << alpha2num[s]) << weekday * 16
    return byte_slot



# like 108-1
semester = sys.argv[1] + '-' + sys.argv[2]

courses = []
courseExtU = []
courseTypeU = []
courseBriefU = []
courseBriefNewU = []
classroomU = list()

# TODO Department, Permanent, Course, Teacher relationships
# TODO create courseExt, courseType, brief?   grade想拔掉
# TODO create own rule: time_slot
for raw_course in raw_courses:
    cos_time = raw_course['cos_time'].split('-')
    time = timeslot_convert(cos_time[0])
    classroom = cos_time[1]
    course = {
        'name': raw_course['cos_cname'],
        'ename': raw_course['cos_ename'],
        'code': raw_course['cos_code'],
        'credict': raw_course['cos_credit'],
        'hours': raw_course['cos_hours'],
        'cid': raw_course['cos_id'],
        'registration_count': raw_course['reg_num'],
        'registration_limit': raw_course['num_limit'],
        'semester': semester,
        'memo': raw_course['memo'],
        'classroom': classroom,
        'time_slot': time
    }
    courses.append(course)
    forien_key_chk(courseTypeU, 'cos_type', raw_course)
    forien_key_chk(courseExtU, 'cos_typeext', raw_course)
    forien_key_chk(courseBriefU, 'brief', raw_course)
    forien_key_chk(courseBriefNewU, 'brief_new', raw_course)
    forien_key_chk(classroomU, 'classroom', course)

print('cos_type unique', courseTypeU)
print('cos_typeext unique', courseExtU)
print('brief unique', courseBriefU)
print('brief_new unique', courseBriefNewU)
# print(courses)
