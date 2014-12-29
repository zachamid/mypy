#!/usr/bin/python

import cgi, cgitb
import os
import ast
import json
import MySQLdb
import MySQLdb.cursors
import db_connection
import xml
import task_delivery

def judge_correctness(id, code):
	exec(code)
	print '</br>'
	py = task_delivery.get_python_code_from_file(id, 'task_complete.py')
	exec(py['task_complete.py'])
	print '</br>'

def judge_similarity(id, code):
	print ast.dump(ast.parse(code))
	print '</br>'
	py = task_delivery.get_python_code_from_file(id, 'task_complete.py')
	print ast.dump(ast.parse(py['task_complete.py']))
	print '</br>'

def judge_time(id,code):
	print 'Currently developing time metric algorithm'

def judge_attempts(id, code):
	print 'Currently developing attempt metric algorithm'