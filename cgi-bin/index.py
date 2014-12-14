#!/usr/bin/python

import session, Cookie, cgi, cgitb, os, db_connection, common_components
cgitb.enable()

cookie = session.return_cookie()

print """Content-type: text/html\n\n

<html><head><script src="/jquery-1.11.1.min.js"></script>
<script src="/user_functions.js"></script>
<link href="/bootstrap-3.2.0-dist/css/bootstrap.min.css" rel="stylesheet">
<link href="/general_style.css" rel="stylesheet">
</head><body>"""

if not session.in_session():
	common_components.print_navbar(cookie['id'].value,' ')
else:
	common_components.print_header()
	
print "</body></html>"