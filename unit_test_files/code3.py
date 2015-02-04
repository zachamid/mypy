#!/usr/bin/env python

def check_multiples(number, base):
	if number % base == 0:
		return 1
	else:
		return 0
		
for x in xrange(1,10):
	mult = dict()
	for y in (2,3,5):
		mult[str(y)] = check_multiples(x,y)
	print '%d:%d:%d' % (mult['2'],mult['3'],mult['5'])