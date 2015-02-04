#!/usr/bin/env python

def check_multiples(number, base):
	if number % base == 0:
		return 1
	else:
		return 0
		
for x in xrange(1,10):
	print '%d:%d:%d' % (check_multiples(x, 2),check_multiples(x, 3),check_multiples(x, 5))