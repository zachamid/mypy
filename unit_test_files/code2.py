#!/usr/bin/env python

def check_multiples(number):
	res = dict()
	if number % 2 == 0:
		res['2'] = 1
	else:
		res['2'] = 0
	if number % 3 == 0:
		res['3'] = 1
	else:
		res['3'] = 0
	if number % 5 == 0:
		res['5'] = 1
	else:
		res['5'] = 0
	return res
		
for x in xrange(1,10):
	mult = check_multiples(x)
	print '%d:%d:%d' % (mult['2'],mult['3'],mult['5'])