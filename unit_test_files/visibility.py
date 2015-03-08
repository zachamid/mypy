#!/usr/bin/python

from splinter import Browser
import time

browser = Browser('zope.testbrowser')
url = 'http://webvm.cs.man.ac.uk/'
sites = [
	'correction_page.py',
	'league_table.py',
	'playground.py',
	'sign_up.py',
	'task_list.py',
	'task_page.py',
	'user_page.py',
	'/teacher/class_results.py',
	'/teacher/index.py',
	'/teacher/sign_up.py',
	'/teacher/site_admin.py',
	'/teacher/task_admin.py',
	'/teacher/task_creator.py'
]

for site in sites:
	browser.visit(url+site)
	browser.reload()
	print browser.title
	
print '\n\nWith Student Credentials:'
browser.cookies.add({'type': 'Student'})
browser.cookies.add({'id': '3'})
print browser.cookies.all()

for site in sites:
	browser.visit(url+site)
	browser.reload()
	print browser.title

print '\n\nWith Teacher Credentials:'
browser.cookies.add({'type': 'Teacher'})
browser.cookies.add({'id': '2'})
print browser.cookies.all()

for site in sites:
	browser.visit(url+site)
	browser.reload()
	print browser.title
	
print '\n\nWith Administrator Credentials:'
browser.cookies.add({'type': 'Teacher'})
browser.cookies.add({'id': '3'})
print browser.cookies.all()

for site in sites:
	browser.visit(url+site)
	browser.reload()
	print browser.title