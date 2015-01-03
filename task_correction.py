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
			fields[name] = val
	print fields
	code = dict()
	for field in fields:
		if isinstance(fields[field], list):
			for item in fields[field]:
				if isinstance(item, ast.AST):
					code[item.__class__.__name__] = ast2dict(item)
					print '(length:'+str(len(code[item.__class__.__name__]))+')'
		if isinstance(fields[field], ast.AST):
			code[fields[field].__class__.__name__] = ast2dict(fields[field])
			print '(length:'+str(len(code[fields[field].__class__.__name__]))+')'
		if isinstance(fields[field], basestring) or isinstance(fields[field],int):
			code[field] = fields[field]
	return code

def adapted_jaccard(dict1, dict2):
	union_count = 0
	for field in dict1:
		if field in dict2:
			if type(dict1[field]) is 'dict' and type(dict2[field]) is'dict':
				union_count += adapted_jaccard(dict1[field],dict2[field])
			elif type(dict1[field]) is 'str' and type(dict2[field]) is 'str':
				dist=levenshteinDistance(dict1[field],dict2[field],len(dict1[field]),len(dict2[field]))
				union_count += dist/max([len(dict1[field]),len(dict2[field])])
			elif type(dict1[field]) is 'int' and type(dict2[field]) is 'int':
				dist=abs(dict1[field] - dict2[field])
				union_count += union_count += dist/max([dict1[field],dict2[field]])
			else:
				print 'Type 1 is '+type(dict1[field]) '</br> Type 2 is '+type(dict2[field])
	intersection_count = len(dict1)+len(dict2)-union_count
	return union_count/intersection_count

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
	dict1 = ast2dict(ast.parse(py['task_complete.py']))
	dict2 = ast2dict(ast.parse(code))
	print '</br>'
	print adapted_jaccard(dict1, dict2)
	print '</br>'

def judge_time(id,code):
	print 'Currently developing time metric algorithm'

def judge_attempts(id, code):
	print 'Currently developing attempt metric algorithm'