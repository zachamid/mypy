#!/usr/bin/python

import cgi, cgitb, json, MySQLdb, db_connection, Cookie, common_components,os
from mako.template import Template
from mako.lookup import TemplateLookup

cgitb.enable()

html_header = ''
cursor = db_connection.get_connection()
cookies = Cookie.SimpleCookie(os.environ.get("HTTP_COOKIE",""))
name = ''
type = ''
if cookies.has_key('id') and cookies.has_key('type'):
	html_header += str(cookies)+'\n'
	if cookies['type'].value == 'Student':
		cursor.execute('SELECT FirstName, LastName FROM Student WHERE StudentID=%s' % (str(cookies['id'].value)))
		type = 'Student'
	else:
		cursor.execute('SELECT FirstName, LastName, Administrator FROM Teacher WHERE TeacherID=%s' % (str(cookies['id'].value)))
		type = 'Teacher'
	record = cursor.fetchone()
	if 'Administrator' in record and record['Administrator'] == 1:
		type = 'Administrator'
	name = record['FirstName']+' '+record['LastName']
html_header += 'Content-type: text/html\n\n'

cursor.execute('SELECT TutorialID, TutorialName FROM Tutorial ORDER BY TutorialID')
tutorials = cursor.fetchall()

include_lookup = TemplateLookup(directories=[os.getcwd()])
if type == 'Teacher':
	include_lookup = TemplateLookup(directories=[os.getcwd()+'/teacher'])

template_file = open('playground_template.html','r')

template = template_file.read()
page_template = Template(template, lookup=include_lookup)
print page_template.render(html_header=html_header, name=name, tutorials=tutorials, type=type)