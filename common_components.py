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
	<button type="button" class="btn btn-default btn-sm" onclick="location.href='sign_up.py'">
  	<span class="glyphicon glyphicon-user"></span> Sign Up
	</button>
    </br><div id="error_space"></div>
  	</div>
  	</div>
  	</div>"""

def print_header_teacher():
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
    <button type="button" class="btn btn-default btn-sm" onclick="validate_login('Teacher')">
  	<span class="glyphicon glyphicon-log-in"></span> Login
	</button>&nbsp&nbsp
	<button type="button" class="btn btn-default btn-sm" onclick="location.href='sign_up.py'">
  	<span class="glyphicon glyphicon-user"></span> Sign Up
	</button>
    </br><div id="error_space"></div> 
  	</div>
  	</div>
  	</div>
	"""
	
def print_navbar(id, curr_page):
	sql_query = 'SELECT * FROM Student WHERE StudentID='+id
	cursor = db_connection.get_connection()
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
	print '<li><a href="user_page.py">Details</a></li>'
	print '<li><a href="progress_page.py">Progress</a></li>'
	print '<li><a href="task_list.py">Task List</a></li>'
	print '<li><a href="playground.py">Playground</a></li>'
	print '<li><a href="league_table.py">League Table</a></li>'
	print """\n
	</ul><ul class="nav navbar-nav navbar-right">
	<li><a onclick="clear_cookies()"><span class="glyphicon glyphicon-log-out"></span>&nbsp
	Log out</a></li></ul></div></div></nav>"""
	
def print_navbar_teacher(id, curr_page):
	sql_query = 'SELECT * FROM Teacher WHERE TeacherID='+id
	cursor = db_connection.get_connection()
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
	print '<li><a href="/teacher/user_page.py">Details</a></li>'
	print '<li><a href="/teacher/class_results.py">Class Administration</a></li>'
	print '<li><a href="/teacher/task_admin.py">Task Administration</a></li>'
	print '<li><a href="/teacher/task_creator.py">Task Creator</a></li>'
	print '<li><a href="/playground.py">Playground</a></li>'
	if(record['Administrator']==1):
		print '<li><a href="/teacher/site_admin.py">Site Administration</a></li>'
	print """\n
	</ul><ul class="nav navbar-nav navbar-right">
	<li><a onclick="clear_cookies()"><span class="glyphicon glyphicon-log-out"></span>&nbsp
	Log out</a></li></ul></div></div></nav>"""
	
def return_navbar_teacher(id, curr_page):
	sql_query = 'SELECT * FROM Teacher WHERE TeacherID='+id
	cursor = db_connection.get_connection()
	cursor.execute(sql_query)
	record = cursor.fetchone()
	name = record['FirstName']+' '+record['LastName']
	return_string = """\n
	<nav class="navbar navbar-default" role="navigation"><div class="container-fluid">
	<div class="navbar-header">
	<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
	<span class="sr-only">Toggle navigation</span><span class="icon-bar"></span>
	<span class="icon-bar"></span><span class="icon-bar"></span>
	</button>
	<a class="navbar-brand" href="#">"""
	return_string = return_string+name
	return_string = return_string+ """\n</a>
	</div><div id="navbar" class="navbar-collapse collapse">
	<ul class="nav navbar-nav">
	"""
	return_string = return_string+ '<li><a href="/teacher/user_page.py">Details</a></li>'
	return_string = return_string+ '<li><a href="/teacher/class_results.py">Class Administration</a></li>'
	return_string = return_string+ '<li><a href="/teacher/task_admin.py">Task Administration</a></li>'
	return_string = return_string+ '<li><a href="/teacher/task_creator.py">Task Creator</a></li>'
	return_string = return_string+ '<li><a href="/playground.py">Playground</a></li>'
	if(record['Administrator']==1):
		return_string = return_string+ '<li><a href="/teacher/site_admin.py">Site Administration</a></li>'
	return_string = return_string+ """\n
	</ul><ul class="nav navbar-nav navbar-right">
	<li><a onclick="clear_cookies()"><span class="glyphicon glyphicon-log-out"></span>&nbsp
	Log out</a></li></ul></div></div></nav>"""
	return return_string