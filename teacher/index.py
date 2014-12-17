#!/usr/bin/env python

import Cookie, cgi, cgitb, os
import /session, /common_components

cgitb.enable()

string_cookie = os.environ.get('HTTP_COOKIE')
cookie = session.return_cookie()

if session.in_session():
	cookie.load(string_cookie)
	session.print_cookie()
elif cookie['type'].value == 'Student':
	print 'Location:/index.py'
print """Content-type: text/html\n\n

<html><head>
<script src="/jquery-1.11.1.min.js"></script>
<link href="bootstrap-3.2.0-dist/css/bootstrap.min.css" rel="stylesheet">
<script src='user_functions.js'></script>
<link rel="stylesheet" type="text/css" href="general_style.css">
<link href="teacher_style.css" rel="stylesheet">
</head>
	<body>"""
if not session.in_session():
	common_components.print_header_teacher()
else:
	common_components.print_navbar_teacher(cookie['id'].value,'')

print """\n
 
  	</body>
</html>
"""