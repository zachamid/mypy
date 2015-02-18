#!/usr/bin/env python

import Cookie, cgi, cgitb, os,sys,json, dicttoxml
sys.path.append(os.pardir)
import common_components, db_connection

post_data = cgi.FieldStorage()
title = post_data['title'].value
task_json = post_data['task_xml'].value
task_skeleton = post_data['skeleton'].value
task_complete = post_data['complete'].value
result = post_data['result'].value
cursor = db_connection.get_connection()

sql_query = '''INSERT INTO Task (Title)
				VALUES(%s)
			''' % (title)
cursor.execute(sql_query)
id = cursor.lastrowid

os.mkdir('/var/www/tasks/'+id)
task_complete_py = open('/var/www/tasks/'+id+'/task_complete.py','rw')
task_complete_py.write(task_complete)
task_complete_py.close()

task_skeleton_py = open('/var/www/tasks/'+id+'/task_skeleton.py','rw')
task_skeleton_py.write(task_skeleton)
task_skeleton_py.close()

result_txt = open('/var/www/tasks/'+id+'/result.txt','rw')
result_txt.write(result)
result_txt.close()

xml_file = open('/var/www/tasks/'+id+'/info.xml','rw')
task_info = json.loads(task_json).value
task_xml = dicttoxml.dicttoxml(task_info)
xml_file.write(task_xml)
xml_file.close()