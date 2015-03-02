#!/usr/bin/env python

import Cookie, cgi, cgitb, os,sys
sys.path.append(os.pardir)
import common_components,db_connection
from mako.template import Template

cgitb.enable()

cookies = Cookie.SimpleCookie(os.environ.get("HTTP_COOKIE",""))
cursor = db_connection.get_connection()
html_header = ''
name = ''
if cookies.has_key('id') and cookies.has_key('type'):
	html_header += cookies
	if cookies['type'].value == 'Teacher':
		cursor.execute('SELECT * FROM Teacher WHERE TeacherID='+cookies['id'].value)
		record = cursor.fetchone()
		if record['Administrator'] == 0:
			html_header += '\nLocation:index.py'
		else:
			name = record['FirstName'] + ' ' + record['LastName']
	else:
		html_header += '\nLocation:../index.py'
else:
	html_header += '\nLocation:../index.py'
	
template_file = open('site_admin_template.html')
page_template = Template(template_file.read())
print page_template.render(type='Administrator',html_header=html_header, name=name)