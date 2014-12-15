#!/usr/bin/python

import cgi, cgitb, json, MySQLdb, db_connection,os
cgitb.enable()

def retrieve_file_info():
	db = db_connection.get_connection()
	cursor = db.cursor()
	cursor.execute('SELECT * FROM Task')
	tasks = cursor.fetchall()
	file_existence_matrix = dict()
	dir = '../tasks'
	directories = [x[0] for x in os.walk(dir)]
	for task in tasks:
		new_dir = ''.join(dir,'/',task['TaskID'])
		if new_dir in directories:
			file_existence_matrix[task['TaskID']]['directory'] = 1
			files = [x[2] for x in os.walk(new_dir)]
			for file in ['info.xml','task_skeleton.py','task_complete.py']:
				if file in files:
					file_existence_matrix[task['TaskID']][file] = 1
		else:
			file_existence_matrix[task['TaskID']]['directory'] = 0
	print file_existence_matrix

retrieve_file_info()