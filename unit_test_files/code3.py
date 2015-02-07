#!/usr/bin/env python

for x in xrange(1,10):
	val2 = 0
	val3 = 0
	val5 = 0
	if x % 2 == 0:
		val2 = 1
	if x % 3 == 0:
		val3 = 1
	if x % 5 == 0:
		val5 = 1
	print '%d:%d:%d' % (val2,val3,val5)