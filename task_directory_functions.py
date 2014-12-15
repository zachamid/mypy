#!/usr/bin/python

import cgi, cgitb, json, MySQLdb, db_connection
cgitb.enable()

def retrieve_file_info():
	db = db_connection.get_connection()
	cursor = db.cursor()
	cursor.execute('SELECT * FROM Task')
	file_existence_matrix = dict()
	directories = [x[0] for x in os.walk('../tasks')]
	print directories

retrieve_file_info()