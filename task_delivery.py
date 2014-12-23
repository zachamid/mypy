#!/usr/bin/python

import cgi, cgitb
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
	

def get_file_info():
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



def get_task_xml(id):
	new_path = path+str(id)+"/info.xml"
	try:
		info = xmltodict.parse(open(new_path, "r"))
		return info
	except IOError:
		error = dict()
		error['Error'] = 'File Not Found'
		error['Description'] = 'file "'+new_path+'" Not Found'
		return error
	except xml.parsers.expat.ExpatError as e:
		error = dict()
		error['Error'] = 'XML Error'
		error['Description'] = e.args[0]
		return error

def get_python_code_from_file(task_id, file_name):
	file_path = path+str(task_id)+"/"+file_name
	try:
		f = open(file_path,'r')
		ret = dict()
		ret[file_name] = f.read()
		return ret 
	except IOError:
		error = dict()
		error['Error'] = 'File Not Found'
		error['Description'] = 'File "'+file_path+'" Not Found'
		return error

def get_compile_code(task_id, given_code):
	xml_data = get_task_xml()['task']
	ret_dict = dict()
	if('Error' in xml_data or 'testcase' not in xml_data):
		ret_dict['code'] = given_code
	else:
		compile_code = given_code+"\n\n\n"
		for testcase in xml_data['test_case']:
			compile_code += """print "TestCase %s: %s(%s)"\n """,
			(testcase['description'],xml_data['method'],str(testcase['args']))
			compile_code += """%s(%s)\n""",(xml_data['method'],str(testcase['args']))
		ret_dict['code'] = compile_code
	return ret_dict