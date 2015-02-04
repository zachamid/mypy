#!/usr/bin/env python

def check_multiples(number):
	ans = dict()
	if number % 2 == 0:
		ans['2'] = 1
	else:
		ans['2'] = 0
	if number % 3 == 0:
		ans['3'] = 1
	else:
		ans['3'] = 0
	if number % 5 == 0:
		ans['5'] = 1
	else:
		ans['5'] = 0
	return ans
		
for x in xrange(1,10):
	mult = check_multiples(x)
	print '%d:%d:%d' % (mult['2'],mult['3'],mult['5'])