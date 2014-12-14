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
	curr = session.get_session()
	print curr['id']
	session.set_session(curr['id']+1, curr['type'])
	


print "</body></html>"