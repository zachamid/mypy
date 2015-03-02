#!/usr/bin/env python

import Cookie, cgi, cgitb, os,sys
sys.path.append(os.pardir)
import common_components
from mako.template import Template

cgitb.enable()

cookies = Cookie.SimpleCookie(os.environ.get("HTTP_COOKIE",""))
html_header = ''
type = 'Teacher'
if cookies.has_key('id') and cookies.has_key('type'):
	html_header += str(cookies)
	if cookies['type'].value == 'Teacher':
		html_header += '\nLocation:../index.py'
		cursor.execute('SELECT * FROM Teacher WHERE TeacherID='+cookies['id'].value)
		record = cursor.fetchone()
		if record['Administrator'] == 0:
			type = 'Administrator'
		else:
		name = record['FirstName'] + ' ' + record['LastName']
else:
	html_header += '\nLocation: index.py'

include_lookup = TemplateLookup(directories=[os.getcwd()])
template_file = open('uses_page_template.html')
page_template = Template(template_file.read())
print page_template.render(html_header=html_header, name=name, type=type)