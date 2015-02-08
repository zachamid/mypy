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
	task_id = posted_data['task_id'].value
	print json.dumps(task_delivery.get_task_info(task_id))
elif str(cmd) == "Get_Task_DB_Info":
	task_info = get_task_list()
	print json.dumps(task_info)
elif str(cmd) == "Get_Task_XML_Info":
	task_id = posted_data['task_id'].value
	xml_info = task_delivery.get_task_xml(task_id)
	print json.dumps(xml_info)
elif str(cmd) == "Get_Task_Python_File":
	task_id = posted_data['task_id'].value
	file_name = posted_data['file_name'].value
	file_content = task_delivery.get_python_code_from_file(task_id, file_name)
	print json.dumps(file_content)
elif str(cmd) == "Get_Task_Compile_Code":
	task_id = posted_data['task_id'].value
	given_code = posted_data['code'].value
	compile_code = task_delivery.get_compile_code(task_id, given_code)
	print json.dumps(compile_code)
elif str(cmd) == "Save_Code":
	task_id = posted_data['task_id'].value
	given_code = posted_data['code'].value
	student_id = posted_data['student_id'].value
	task_delivery.save_code(given_code, task_id, student_id)