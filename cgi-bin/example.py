#!/usr/bin/python

import cgi
import cgitb
import json
import MySQLdb
import MySQLdb.cursors
import session
cgitb.enable()

session.print_session()
print """content-type: text/html

<html><body>
"""


if(session.is_set()):
	session.set_session(curr['id']+1, curr['type'])
else:
	print 'Yellow</br>'
	session.set_session(0,'Student')

session.print_session()

print "</body></html>"