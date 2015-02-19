#!/usr/bin/env python

import Cookie, cgi, os,sys,json, dicttoxml
sys.path.append(os.pardir)
import common_components, db_connection

print "Content-type: text/html\n\n"
post_data = cgi.FieldStorage()
title = post_data['title'].value
task_json = post_data['task_xml'].value
task_skeleton = post_data['skeleton'].value
task_complete = post_data['complete'].value
result = post_data['result'].value
cursor = db_connection.get_connection()

sql_query = '''INSERT INTO Task (Title)
				VALUES('%s')
			''' % (title)
cursor.execute(sql_query)
id = cursor.lastrowid

path = '/var/www/tasks/'+str(id)
os.mkdir(path)
task_complete_py = open(path+'/task_complete.py','w')
task_complete_py.write(task_complete)
task_complete_py.close()

task_skeleton_py = open(path+'/task_skeleton.py','w')
task_skeleton_py.write(task_skeleton)
task_skeleton_py.close()

result_txt = open(path+'/result.txt','w')
result_txt.write(result)
result_txt.close()

xml_file = open(path+'/info.xml','w')
task_info = json.loads(task_json)
task_xml = dicttoxml.dicttoxml(task_info,ids=True)
xml_file.write(task_xml)
xml_file.close()