#!/usr/bin/python

import cgi, cgitb, task_delivery
import os
import json
import MySQLdb
import MySQLdb.cursors
import db_connection
import xml
import xmltodict
import task_delivery
cgitb.enable()

posted_data = cgi.FieldStorage()
cmd = posted_data['cmd'].value

print """content-type:text/html

"""
if str(cmd) == "Get_Task_File_Info":
	file_info = task_delivery.get_file_info()
	print json.dumps(file_info)
elif str(cmd) == "Task_Info":
	task_id = posted_data['params'].value
	print json.dumps(task_delivery.get_task_info(task_id))
elif str(cmd) == "Get_Task_DB_Info":
	task_info = get_task_list()
	print json.dumps(task_info)
elif str(cmd) == "Get_Task_XML_Info":
	task_id = posted_data['params'].value
	xml_info = task_delivery.get_task_xml(task_id)
	print json.dumps(xml_info)
elif str(cmd) == "Get_Task_Python_File":
	task_id = posted_data['params'].value
	file_name = posted_data['params_2'].value
	file_content = task_delivery.get_python_code_from_file(task_id, file_name)
	print json.dumps(file_content)
elif str(cmd) == "Get_Task_Compile_Code":
	task_id = posted_data['params'].value
	file_content = task_delivery.get_python_code_from_file(task_id,'task_skeleton.py')
	compile_code = task_delivery.get_compile_code(task_id, file_content['task_skeleton.py'])
	print json.dumps(compile_code)