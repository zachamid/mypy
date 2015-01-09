#!/usr/bin/python

import ast

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

def similarity_index_per_item(item1, item2):
	if type(item1)==str and type(item2)==str:
		return levenshteinIndex(item1,item2)
	if (type(item1)==int and type(item1)==int) or (type(item1)==float and type(item2)==float) or (type(item1)==long and type(item2)==long):
		return 1-abs((float)(item1 - item2))/max([item1,item2])
	if type(item1)==bool and type(item2)==bool:
		if item1 == item2:
			return 1
		else:
			return 0
	if (type(item1)==dict and type(item2)==dict) or (type(item1)==list and type(item2)==list):
		distance = jaccard(item1,item2)
		return distance
		
def levenshteinIndex(str1,str2):
	distance = levenshteinDistance(str1,str2,len(str1),len(str2))
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
	
def jaccard(dict1, dict2, level=0):
	intersection = 0
	if(len(dict1)==0 and len(dict2)==0):
		return 1
	if(len(dict1)==0 or len(dict2)==0):
		return 0
	if type(dict1)==dict and type(dict2)==dict:
		for field in dict1:
			if field in dict2:
				intersection += similarity_index_per_item(dict1[field], dict2[field])
	else:
		for x in xrange(0,min([len(dict1),len(dict2)])):
			intersection += similarity_index_per_item(dict1[x], dict2[x])
			
	union = len(dict1)+len(dict2)-intersection
	return (float)(intersection/union)

code = """for x in xrange(0,13):print x
"""
code2 = """for x in xrange(0,13):
	print x
"""

dict1 = ast2dict(ast.parse(code))
print dict1
dict2 = ast2dict(ast.parse(code2))
print dict2
print jaccard(dict1,dict2)