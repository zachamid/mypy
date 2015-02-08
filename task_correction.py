#!/usr/bin/python

import cgi, cgitb, os, ast, json, xml, pylev, math

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
		if isinstance(fields[field], ast.AST):
			code[fields[field].__class__.__name__] = ast2dict(fields[field])
		if isinstance(fields[field], basestring) or isinstance(fields[field],int):
			code[field] = fields[field]
	return code

def similarity_index_per_item(item1, item2):
	if type(item1)==str and type(item2)==str:
		return pylev.levenshtein(item1,item2)
	if ((type(item1)==int and type(item1)==int)
			or (type(item1)==float and type(item2)==float) 
			or (type(item1)==long and type(item2)==long)):
		return (abs((float)(item1 - item2)))/float(max([item1+1,item2+1]))
	if type(item1)==bool and type(item2)==bool:
		if item1 == item2:
			return 0
		else:
			return 1
	if (type(item1)==dict and type(item2)==dict) or (type(item1)==list and type(item2)==list):
		return 1-jaccard(item1,item2)
		
def levenshteinIndex(str1,str2):
	distance = pylev.levenshtein(str1,str2)
	return 1-(float)(distance)/max([len(str1),len(str2)])

def ast2dict(node):
	fields = dict()
	for name, val in ast.iter_fields(node):
		if name not in ('left', 'right'):
			fields[name] = val
	code = dict()
	for field in fields:
		if isinstance(fields[field], list):
			for item in fields[field]:
				if isinstance(item, ast.AST):
					code[item.__class__.__name__] = ast2dict(item)
		if isinstance(fields[field], ast.AST):
			code[fields[field].__class__.__name__] = ast2dict(fields[field])
		if isinstance(fields[field], basestring) or isinstance(fields[field],int):
			code[field] = fields[field]
	return code
	
def jaccard(dict1, dict2):
	intersection = 0.0
	if(len(dict1)==0 and len(dict2)==0):
		return 1
	if(len(dict1)==0 or len(dict2)==0):
		return 0
	if type(dict1)==dict and type(dict2)==dict:
		for field in dict1:
			if field in dict2:
				diff = similarity_index_per_item(dict1[field], dict2[field])
				print '%s:%s => %d' % (str(dict1[field]), str(dict2[field]), diff)
				intersection += 1-(0.4 * diff)
			
	union = len(dict1)+len(dict2)-intersection
	return (float)(intersection/union)

def judge_correctness(desired_output, submitted_output):
	#return levenshteinIndex(desired_output, submitted_output)
	return levenshteinIndex(desired_output, submitted_output)

def teachers_report(code1,code2):
	code1 = code1.split('\n')
	code2 = code2.split('\n')
	C = longest_common_subsequence(code1, code2)
	printDiff(C, code1, code2, len(code1), len(code2))

def longest_common_subsequence(code1, code2):
	len1 = len(code1)
	len2 = len(code2)
	C=[[0 for j in range(len2+1)] for i in range(len1+1)]
	for i in range(1, len1+1):
		for j in range(1,len2+1):
			if code1[i-1] == code2[j-1]: 
				C[i][j] = C[i-1][j-1] + 1
			else:
				C[i][j] = max(C[i][j-1], C[i-1][j])
	return C

def printDiff(C, X, Y, i, j):
	if i > 0 and j > 0 and X[i-1] == Y[j-1]:
		printDiff(C, X, Y, i-1, j-1)
		print "  " + X[i-1]
	else:
		if j > 0 and (i == 0 or C[i][j-1] >= C[i-1][j]):
			printDiff(C, X, Y, i, j-1)
			print "+ " + Y[j-1]
		elif i > 0 and (j == 0 or C[i][j-1] < C[i-1][j]):
			printDiff(C, X, Y, i-1, j)
			print "- " + X[i-1]

def compare_asts(desired_code, submitted_code):
	dict1 = ast2dict(ast.parse(desired_code))
	dict2 = ast2dict(ast.parse(submitted_code))
	print str(dict1) + '</br>' + str(dict2) + '</br>'
	print jaccard(dict1, dict2)

def quickest_time(times):
	min_time = float('inf')
	for time in times:
		delta = date['DateCompleted']-date['DateStarted']
		if min_time > delta.total_seconds():
			min_time = delta
	return min_time

def judge_time(min_time, time):
	return float(min_time/time)

def judge_attempts(attempts):
	return float(1/math.sqrt(attempts))