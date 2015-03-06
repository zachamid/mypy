#!/usr/bin/python

import cgi, cgitb, json, MySQLdb, db_connection, Cookie, common_components,os
from mako.template import Template
from mako.lookup import TemplateLookup

cgitb.enable()

html_header = ''  
cookies = Cookie.SimpleCookie(os.environ.get("HTTP_COOKIE",""))
if cookies.has_key('id') and cookies.has_key('type'):
	html_header += cookies
	html_header += 'Location: user_page.py'

sql = '''SELECT ClassID, ClassName FROM Class'''
cursor = db_connection.get_connection()
cursor.execute(sql)
classes = cursor.fetchall()

include_lookup = TemplateLookup(directories=[os.getcwd()])
template_file = open('sign_up_template.html','r')
template = template_file.read()
page_template = Template(template, lookup=include_lookup)
print page_template.render(html_header=html_header, classes=classes)