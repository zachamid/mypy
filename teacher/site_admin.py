import Cookie, cgi, cgitb, os,sys
sys.path.append(os.pardir)
import session,common_components,db_connection

cgitb.enable()

string_cookie = os.environ.get('HTTP_COOKIE')
cookie = session.return_cookie()
cursor = db_connection.get_connection()
print 'Content-type: text/html'
if session.in_session():
	if cookie['type'].value == 'Teacher':
		cursor.execute('SELECT * FROM Teacher WHERE TeacherID='+cookie['id'].value)
		record = cursor.fetchone()
		if record['Administrator'] == 0:
			print 'Location: index.py'
	else:
		print 'Location: ../index.py'
else:
	print 'Location: ../index.py'
	
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
common_components.print_navbar_teacher(cookie['id'].value, 'site_admin')
print """\n
		<div class="container col-sm-12 col-md-12"><div class="panel panel-default">
			Create Classes
		</div></div>
		<div class="container col-sm-12 col-md-12"><div class="panel panel-default">
			Manage Teachers
		</div></div>
		<div class="container col-sm-12 col-md-12"><div class="panel panel-default">
			Accept Requests
		</div></div>
	</body>
</html>
"""