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
	directories = [x[1] for x in os.walk(dir)]
	#for task in tasks:
	#	if ''.join(dir,'/',task['TaskID']):
	#		file_existence_matrix[task['TaskID']]['directory'] = 1
#			files = 
	#	else:
	#		file_existence_matrix[task['TaskID']]['directory'] = 0
	print directories

retrieve_file_info()