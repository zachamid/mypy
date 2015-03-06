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
	html_header += str(cookies)
	cursor.execute('SELECT FirstName, LastName FROM %s WHERE %sID=%s' % (cookies['type'].value,cookies['type'].value,str(cookies['id'].value)))
	record = cursor.fetchone()
	name = record['FirstName']+' '+record['LastName']
	type = cookies['type'].value

cursor.execute('SELECT TutorialID, TutorialName FROM Tutorials')
tutorials = cursor.fetchall()

include_lookup = TemplateLookup(directories=[os.getcwd()])
if type == 'Teacher':
	include_lookup = TemplateLookup(directories=[os.getcwd()+'/teacher'])
	
template_file = open('playground_template.html','r')

template = template_file.read()
page_template = Template(template, lookup=include_lookup)
print page_template.render(html_header=html_header, name=name, tutorials=tutorials, type=type)