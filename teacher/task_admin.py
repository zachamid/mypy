#!/usr/bin/python

import Cookie, cgi, cgitb, os,sys
sys.path.append(os.pardir)
import common_components, db_connection
from mako.template import Template
from mako.lookup import TemplateLookup

cgitb.enable()

cookies = Cookie.SimpleCookie(os.environ.get("HTTP_COOKIE",""))
html_header = ''
name = ''
type = ''
cursor = db_connection.get_cursor()


if cookies.has_key('id') and cookies.has_key('type'):
	html_header += str(cookies)
	if cookies['type'].value == 'Teacher':
		html_header += 'Location:index.py'
		cursor.execute('SELECT * FROM Teacher WHERE TeacherID='+cookies['id'].value)
		record = cursor.fetchone()
		type = 'Teacher'
		if record['Administrator'] == 0:
			type = 'Administrator'
		name = record['FirstName'] + ' ' + record['LastName']
else:
	html_header += 'Location: ../index.py'

include_lookup = TemplateLookup(directories=[os.getcwd()])
template_file = open('task_admin_template.html')
page_template = Template(template_file.read(), lookup=include_lookup)
print page_template.render(html_header=html_header, name=name, type=type)