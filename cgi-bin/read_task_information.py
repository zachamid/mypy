#!/usr/bin/python

import cgi
import cgitb
import os
import json
import MySQLdb
import MySQLdb.cursors
import db_connection
cgitb.enable()

global path = '../../tasks/'

def get_task_list():
	db = db_connection.get_connection()
	cursor = db.cursor()
	sql = 'SELECT * FROM Task'
	cursor.execute(sql)
	out = cursor.fetchall()
	return out
	

def retrieve_file_info():
	tasks = get_task_list()
	files = os.listdir(path)
	file_info = dict()
	for task in tasks:
		file_info['taskID'] = dict()
		if task['taskID'] in files:
			file_info['taskID']['directory'] = 1
			new_path=path+task['taskID']+"/"
			task_files=os.listdir(new_path)
			if 'info.xml' in task_files:
			 	file_info['taskID']['info.xml'] = 1
			else:
			 	file_info['taskID']['info.xml'] = 0
		else:
			file_info['taskID']['directory'] = 0
	return file_info
	
	
#db = db_connection.get_connection()
#posted_data = cgi.FieldStorage()
#cmd = posted_data['cmd'].value




print """content-type:text/html

<html><body>
"""

print json.dumps(retrieve_file_list)

print "</body></html>"