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
import subprocess

def levenshteinDistance(str1,str2,len1,len2):
	if len1 == 0:
		return len2
	if len2 == 0:
		return len1
	
	cost = 1
	if str1[len1-1]==str2[len2-1]:
		cost = 0
	
	return min(levenshteinDistance(str1,str2,len1-1,len2)+1,
	levenshteinDistance(str1,str2,len1,len2-1)+1,
	levenshteinDistance(str1,str2,len1-1,len2-1)+cost)

def judge_correctness(task_id,student_id, code):
	task_delivery.save_to_file(task_id,student_id, code)
	filename = task_delivery.path+str(task_id)+'/'+str(student_id)+'.py'
	user_code = subprocess.Popen(['python', filename], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	print '</br>'
	set_code = eval('python '+'../tasks/'+task_id+'/task_complete.py')
	print '</br>'
	print 'Levenshtein Distance: '+ str(levenshteinDistance(user_code,set_code, len(user_code), len(set_code)))

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