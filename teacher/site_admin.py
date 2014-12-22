#!/usr/bin/env python

import Cookie, cgi, cgitb, os,sys
sys.path.append(os.pardir)
import common_components,db_connection

cgitb.enable()

cookies = Cookie.SimpleCookie(os.environ.get("HTTP_COOKIE",""))
cookie = session.return_cookie()
cursor = db_connection.get_connection()
print 'Content-type: text/html'
if cookies.has_key('id') and cookies.has_key('type'):
	print os.environ.get("HTTP_COOKIE","")
	if cookies['type'].value == 'Teacher':
		cursor.execute('SELECT * FROM Teacher WHERE TeacherID='+cookies['id'].value)
		record = cursor.fetchone()
		if record['Administrator'] == 0:
			print 'Location:index.py'
	else:
		print 'Location:../index.py'
else:
	print 'Location:../index.py'
	
print """\n\n

<html>
	<head>
		<script src="../jquery-1.11.1.min.js"></script>
  		<script src='../user_functions.js'></script>
  		<title>Teacher Portal: Site Administration</title>
  		<link href="../bootstrap-3.2.0-dist/css/bootstrap.min.css" rel="stylesheet">
  		<link href="../general_style.css" rel="stylesheet">
  		<link href="teacher_style.css" rel="stylesheet">
	</head>
	<body>"""
common_components.print_navbar_teacher(cookies['id'].value, 'site_admin')
print """\n
		<div class="container col-sm-12 col-md-12"><div class="panel panel-default translucent">
			Create Classes
		</div></div>
		<div class="container col-sm-12 col-md-12"><div class="panel panel-default translucent">
			Manage Teachers
		</div></div>
		<div class="container col-sm-12 col-md-12"><div class="panel panel-default translucent">
			Accept Requests
		</div></div>
	</body>
</html>
"""