import json
import sys
import csv
import urllib.request
import os
from config import teacher_url

if teacher_url == "":
    print("please config url")
    exit(0)

if len(sys.argv) != 2:
    print("please input the year to be imported")
    exit(0)

with urllib.request.urlopen(teacher_url + '?acy=' + sys.argv[1]) as url:
    teachers = json.loads(url.read().decode(encoding='utf-8'))

file = 'teacher_' + sys.argv[1] + '.csv'

keys = ['real_id', 'name']

outFile = open(file, 'w')
out = csv.writer(outFile, quoting=csv.QUOTE_ALL)
out.writerow(keys)

for t in teachers:
    out.writerow(t.values())

os.system('sudo mv {0} /var/lib/mysql-files/{0}'.format(file))
