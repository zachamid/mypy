#!/usr/bin/env python

import Cookie, cgi, cgitb, os,sys
sys.path.append(os.pardir)
import common_components,db_connection
from mako.template import Template
from mako.lookup import TemplateLookup

cgitb.enable()

cookies = Cookie.SimpleCookie(os.environ.get("HTTP_COOKIE",""))
cursor = db_connection.get_connection()
html_header = ''
name = ''
if cookies.has_key('id') and cookies.has_key('type'):
	html_header += str(cookies)
	if cookies['type'].value == 'Teacher':
		cursor.execute('SELECT * FROM Teacher WHERE TeacherID='+cookies['id'].value)
		record = cursor.fetchone()
		if record['Administrator'] == 0:
			html_header += '\nLocation:index.py'
		else:
			name = record['FirstName'] + ' ' + record['LastName']
	else:
		html_header += 'Location:../index.py'
else:
	html_header += 'Location:../index.py'

include_lookup = TemplateLookup(directories=[os.getcwd()])
template_file = open('site_admin_template.html')
page_template = Template(template_file.read(), lookup=include_lookup)
print page_template.render(type='Administrator',html_header=html_header, name=name)