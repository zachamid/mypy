#!/usr/bin/python

import cgi, cgitb
import os
import ast
import json
import MySQLdb
import MySQLdb.cursors
import db_connection
import xml
import read
import task_delivery

def judge_correctness(id, code):
	exec(code)
	exec(get_python_code_from_file(id, 'task_complete.py'))

def judge_similarity(id, code):
	print ast.parse(code)
	print ast.parse(get_python_code_from_file(id, 'task_complete.py'))

def judge_time(id,code):
	print 'Currently developing time metric algorithm'

def judge_attempts(id, code):
	print 'Currently developing attempt metric algorithm'