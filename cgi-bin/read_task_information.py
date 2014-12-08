#!/usr/bin/python

import cgi
import cgitb
import os
import json
import MySQLdb
import MySQLdb.cursors
import db_connection
cgitb.enable()


path = '../../tasks/'

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
		file_info[task['TaskID']] = dict()
		flag = 0
		for file in files:
			if file == task['TaskID']:
				print task['TaskID'] + " " + file+"</br>"
				flag = 1
		if flag:
			file_info[task['TaskID']]['directory'] = 1
			new_path=path+task['TaskID']+"/"
			task_files=os.listdir(new_path)
			if 'info.xml' in task_files:
			 	file_info[task['TaskID']]['info.xml'] = 1
			else:
			 	file_info[task['TaskID']]['info.xml'] = 0
		else:
			file_info[task['TaskID']]['directory'] = 0
	return file_info
	
	
#db = db_connection.get_connection()
#posted_data = cgi.FieldStorage()
#cmd = posted_data['cmd'].value




print """content-type:text/html

<html><body>
"""
file_info = retrieve_file_info()
print json.dumps(file_info)

print "</body></html>"