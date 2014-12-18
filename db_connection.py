#!/usr/bin/python

import cgi
import cgitb
import json
import MySQLdb
import MySQLdb.cursors
cgitb.enable()

def get_connection():
	db = MySQLdb.connect('localhost','root','S0crat3s34!','test', cursorclass=MySQLdb.cursors.DictCursor)
	cursor = db.cursor()
	return cursor