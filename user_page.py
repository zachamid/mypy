#!/usr/bin/python

import cgi, cgitb, json, MySQLdb, db_connection,Cookie, common_components,os
from mako.template import Template
from mako.lookup import TemplateLookup

cgitb.enable()

cookies = Cookie.SimpleCookie(os.environ.get("HTTP_COOKIE",""))
html_header = ''
name = ''
person_record = {'StudentID': -1, 'FirstName':'', 'LastName': '', 'Email':'', 'ClassName':''}
if cookies.has_key('id') and cookies.has_key('type'):
	html_header += str(cookies)
	cursor = db_connection.get_connection()
	sql = '''SELECT StudentID, FirstName, LastName, Email, Class.ClassName
		 FROM Student
		 LEFT JOIN Class
		 ON Class.ClassID = Student.ClassID
		 WHERE StudentID='''+cookies['id'].value
	cursor.execute(sql)
	person_record = cursor.fetchone()
	name = person_record['FirstName']+' '+person_record['LastName']
	if person_record['ClassName']==None:
		person_record['ClassName'] = 'Unassigned'
else:
	html_header +=  'Location:index.py'
	
include_lookup = TemplateLookup(directories=[os.getcwd()])
template_file = open('user_page_template.html')
page_template = Template(template_file.read(), lookup=include_lookup)
print page_template.render(html_header=html_header, name=name, person_record=person_record)