#!/usr/bin/env python

import Cookie, cgi, cgitb, os,sys
sys.path.append(os.pardir)
import common_components, db_connection
from mako.template import Template
from mako.lookup import TemplateLookup

cgitb.enable()

cookies = Cookie.SimpleCookie(os.environ.get("HTTP_COOKIE",""))
cursor = db_connection.get_connection()
html_header = ''
name = ''
type = ''
if cookies.has_key('id') and cookies.has_key('type'):
	html_header += str(cookies)
	if cookies['type'].value == 'Teacher':
		cursor.execute('SELECT FirstName, LastName FROM Teacher WHERE ' + cookies['id'].value)
		record = cursor.fetchone()
		name = record['FirstName']+' '+record['LastName']
		type = 'Teacher'	
	elif cookies['type'].value == 'Student':
		html_header += 'Location:../index.py'

include_lookup = TemplateLookup(directories=[os.getcwd()])
template_file = open('index.html','r')
template = template_file.read()
page_template = Template(template, lookup=include_lookup)
print page_template.render(html_header=html_header, type=type, name=name)