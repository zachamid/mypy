#!/usr/bin/python

import cgi
import cgitb
import os
import json
import MySQLdb
import MySQLdb.cursors
import db_connection
import xml
import xmltodict
cgitb.enable()


path = '../tasks/'

def get_task_list():
	cursor = db_connection.get_connection()
	sql = 'SELECT * FROM Task'
	cursor.execute(sql)
	out = cursor.fetchall()
	return out
	

def retrieve_file_info():
	tasks = get_task_list()
	files = os.listdir(path)
	file_info = dict()
	for task in tasks:
		file_info[task['TaskID']] = dict()
		if str(task['TaskID']) in files:
			file_info[task['TaskID']]['directory'] = 1
			new_path=path+str(task['TaskID'])+"/"
			task_files=os.listdir(new_path)
			if 'info.xml' in task_files:
			 	file_info[task['TaskID']]['info.xml'] = 1
			else:
			 	file_info[task['TaskID']]['info.xml'] = 0
			 
			if 'task_skeleton.py' in task_files:
			 	file_info[task['TaskID']]['task_skeleton.py'] = 1
			else:
			 	file_info[task['TaskID']]['task_skeleton.py'] = 0
			
			if 'task_complete.py' in task_files:
			 	file_info[task['TaskID']]['task_complete.py'] = 1
			else:
			 	file_info[task['TaskID']]['task_complete.py'] = 0
		else:
			file_info[task['TaskID']]['directory'] = 0
	return file_info



def retrieve_task_xml(id):
	new_path = path+str(id)+"/info.xml"
	try:
		info = xmltodict.parse(open(new_path, "r"))
		return info
	except IOError:
		error = dict()
		error['Error_Title'] = 'File Not Found'
		error['Description'] = 'file "'+new_path+'" Not Found'
		return error
	except xml.parsers.expat.ExpatError:
		error = dict()
		error['Error_Title'] = 'XML Error'
		error['Description'] = e['args']
		return error


#db = db_connection.get_connection()
posted_data = cgi.FieldStorage()
cmd = posted_data['cmd'].value

print """content-type:text/html

"""
if str(cmd) == "File_Info":
	file_info = retrieve_file_info()
	print json.dumps(file_info)
elif str(cmd) == "Task_Info":
	task_id = posted_data['params'].value
	print retrieve_task_info(task_id)
elif str(cmd) == "Task_DB_Info":
	task_info = get_task_list()
	print json.dumps(task_info)
elif str(cmd) == "Task_XML":
	task_id = posted_data['params'].value
	xml_info = retrieve_task_xml(task_id)
	print json.dumps(xml_info)

print ""