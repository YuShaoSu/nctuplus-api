import json
import sys
import urllib.request, json

# with open('../model/seed/course.json') as data:
#     raw_courses = json.load(data)

with urllib.request.urlopen("https://dcpc.nctu.edu.tw/plug/n/nctup/CourseList?acy=" + sys.argv[1] + "&sem=" + sys.argv[2]) as url:
    raw_courses = json.loads(url.read().decode())


def forien_key_chk(unique_list, column, c):
    if c[column] not in unique_list:
        unique_list.append(c[column])


# print(raw_courses)

# like 108-1
semester = sys.argv[1] + '-' + sys.argv[2]

courses = []

courseExtU = []
courseTypeU = []
courseBriefU = []
courseBriefNewU = []

# TODO Department, Permanent, Course, Teacher relationships
# TODO create courseExt, courseType, brief?   grade想拔掉
# TODO parse: cos_time(classroom, time_slot)
for raw_course in raw_courses:
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
        'memo': raw_course['memo']
    }
    courses.append(course)
    cos_time = raw_course['cos_time'].split('-')
    time = cos_time[0]
    classroom = cos_time[1]
    forien_key_chk(courseTypeU, 'cos_type', raw_course)
    forien_key_chk(courseExtU, 'cos_typeext', raw_course)
    forien_key_chk(courseBriefU, 'brief', raw_course)
    forien_key_chk(courseBriefNewU, 'brief_new', raw_course)

print('cos_type unique', courseTypeU)
print('cos_typeext unique', courseExtU)
print('brief unique', courseBriefU)
print('brief_new unique', courseBriefNewU)
# print(courses)
