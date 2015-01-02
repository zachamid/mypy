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


def str_node(node):
    if isinstance(node, ast.AST):
        fields = [(name, str_node(val)) for name, val in ast.iter_fields(node) if name not in ('left', 'right')]
        rv = '%s(%s' % (node.__class__.__name__, ', '.join('%s=%s' % field for field in fields))
        return rv + ')'
    else:
        return repr(node)

def ast_visit(node, level=0):
    print('&nbsp&nbsp&nbsp&nbsp' * level + str_node(node)+'</br>')
    for field, value in ast.iter_fields(node):
        if isinstance(value, list):
            for item in value:
                if isinstance(item, ast.AST):
                    ast_visit(item, level=level+1)
        elif isinstance(value, ast.AST):
            ast_visit(value, level=level+1)

def ast2dict(node):
	fields = dict()
	for name, val in ast.iter_fields(node):
		if name not in ('left', 'right'):
			field[name] = val
	code = dict()
	for field in fields:
		if isinstance(fields[field], list):
			for item in fields[field]:
				if isinstance(fields[field], ast.AST):
					code[fields[field].__class__.__name__] = ast2dict(node)
				if isinstance(fields[field], basestring) or isinstance(fields[field],int):
					code[field] = fields[field]
		if isinstance(fields[field], ast.AST):
			code[fields[field].__class__.__name__] = ast2dict(node)
		if isinstance(fields[field], basestring) or isinstance(fields[field],int):
			code[field] = fields[field]
		
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
	dirname = task_delivery.path+str(task_id)+'/'
	user_code = task_delivery.get_python_output(dirname+str(student_id)+'.py')
	print '</br>'+ user_code
	set_code = task_delivery.get_python_output(dirname+'task_complete.py')
	print '</br>'+set_code
	print '</br>Levenshtein Distance: '+ str(levenshteinDistance(user_code,set_code, len(user_code), len(set_code)))

def judge_similarity(id, code):
	py = task_delivery.get_python_code_from_file(id, 'task_complete.py')
	ast_visit(ast.parse(py['task_complete.py']))
	print '</br>'
	ast_visit(ast.parse(code))
	print '</br>'
	print str(ast2dict(ast.parse(code)))
	print '</br>'
	print str(ast2dict(ast.parse(py['task_complete.py'])))
	print '</br>'

def judge_time(id,code):
	print 'Currently developing time metric algorithm'

def judge_attempts(id, code):
	print 'Currently developing attempt metric algorithm'