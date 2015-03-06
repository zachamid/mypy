#!/usr/bin/env python

import Cookie, cgi, cgitb, os,sys
sys.path.append(os.pardir)
import common_components,db_connection
from mako.template import Template
from mako.lookup import TemplateLookup

cgitb.enable()

cursor = db_connection.get_connection()
cookies = Cookie.SimpleCookie(os.environ.get("HTTP_COOKIE",""))
html_header = ''
type = 'Teacher'
if cookies.has_key('id') and cookies.has_key('type'):
	html_header += str(cookies)
	if cookies['type'].value == 'Student':
		html_header += 'Location:../index.py'
	else:
		sql_query = 'SELECT * FROM Teacher WHERE TeacherID='+cookies['id'].value
		cursor.execute(sql_query)
		record = cursor.fetchone()
		name = record['FirstName'] + ' ' + record['LastName']
		if record['Administrator'] == 1:
			type='Administrator'
else:
	html_header += 'Location: index.py'

include_lookup = TemplateLookup(directories=[os.getcwd()])
template_file = open('uses_page_template.html')
page_template = Template(template_file.read(), lookup=include_lookup)
print page_template.render(html_header=html_header, type=type, name=name, person=record)