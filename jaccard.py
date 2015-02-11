#!/usr/bin/python

import ast
from task_correction import *

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