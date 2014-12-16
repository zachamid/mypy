#!/usr/bin/python

import MySQLdb, db_connection

def print_header():
	print """\n
	<div class="jumbotron translucent">
  	<div class="row">
  	<div class="col-md-9">
  	<h1> MyPy</h1></br>
  	<h2> The Online Python Education Tool </h2></br>
  	</div>
  	<div class="col-md-3">
    <input type="email" name="email" class="form-control" id="email_field" placeholder="Email"></br>
    <input type="password" name="pword" class="form-control" id="pword_field" placeholder="Password"></br>
    <button type="button" class="btn btn-default btn-sm" onclick="validate_login('Student')">
  	<span class="glyphicon glyphicon-log-in"></span> Login
	</button>&nbsp&nbsp
	<button type="button" class="btn btn-default btn-sm" onclick="location.href='sign_up.php'">
  	<span class="glyphicon glyphicon-user"></span> Sign Up
	</button>
    </br><div id="error_space"></div>
  	</div>
  	</div>
  	</div>"""

def print_navbar(id, curr_page):
	sql_query = 'SELECT * FROM Student WHERE StudentID='+id
	db = db_connection.get_connection()
	cursor = db.cursor()
	cursor.execute(sql_query)
	record = cursor.fetchone()
	name = record['FirstName']+' '+record['LastName']
	print """\n
	<nav class="navbar navbar-default" role="navigation"><div class="container-fluid">
	<div class="navbar-header">
	<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
	<span class="sr-only">Toggle navigation</span><span class="icon-bar"></span>
	<span class="icon-bar"></span><span class="icon-bar"></span>
	</button>
	<a class="navbar-brand" href="#">"""
	print name
	print """\n</a>
	</div><div id="navbar" class="navbar-collapse collapse">
	<ul class="nav navbar-nav">
	"""
	if(curr_page == 'user_page'):
		print '<li class="active"><a href="#">Details</a></li>'
	else:
		print '<li><a href="user_page.py">Details</a></li>'
	if(curr_page == 'task_list'):
		print '<li class="active"><a href="#">Task_List</a></li>'
	else:
		print '<li><a href="task_list.py">Task_List</a></li>'
	if(curr_page == 'playground'):
		print '<li class="active"><a href="#">Playground</a></li>'
	else:
		print '<li><a href="playground.py">Playground</a></li>'
	
	print """\n
	</ul><ul class="nav navbar-nav navbar-right">
	<li><a onclick="clear_cookies()"><span class="glyphicon glyphicon-log-out"></span>&nbsp
	Log out</a></li></ul></div></div></nav>"""
	
def print_navbar_teacher(id, curr_page):
	sql_query = 'SELECT * FROM Teacher WHERE TeacherID='+id
	db = db_connection.get_connection()
	cursor = db.cursor()
	cursor.execute(sql_query)
	record = cursor.fetchone()
	name = record['FirstName']+' '+record['LastName']
	print """\n
	<nav class="navbar navbar-default" role="navigation"><div class="container-fluid">
	<div class="navbar-header">
	<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
	<span class="sr-only">Toggle navigation</span><span class="icon-bar"></span>
	<span class="icon-bar"></span><span class="icon-bar"></span>
	</button>
	<a class="navbar-brand" href="#">'"""
	print name
	print """\n</a>
	</div><div id="navbar" class="navbar-collapse collapse">
	<ul class="nav navbar-nav">
	"""
	if(curr_page == 'user_page'):
		print '<li class="active">Details</a></li>'
	else:
		print '<li><a href="teacher/user_page.php">Details</a></li>'
	if(curr_page == 'task_list'):
		print '<li class="active">Class Administration</a></li>'
	else:
		print '<li><a href="user_page.php">Class Administration</a></li>'
	if(curr_page == 'playground'):
		print '<li class="active">Task Administration</a></li>'
	else:
		print '<li><a href="user_page.php">Task Administration</a></li>'
	
	print """\n
	</ul><ul class="nav navbar-nav navbar-right">
	<li><a onclick="clear_cookies()"><span class="glyphicon glyphicon-log-out"></span>&nbsp
	Log out</a></li></ul></div></div></nav>"""