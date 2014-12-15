#!/usr/bin/python

import Cookie
import os
import string
import cgi, cgitb

cookie = Cookie.SimpleCookie()

def in_session():
	cookie_string = os.environ.get('HTTP_COOKIE')
	if not cookie_string:
		return 0
	else:
		cookie.load(cookie_string)
		if ('id' in cookie and 'type' in cookie):
			return 1
		else:
			return 0
			
def set_session(type, id):
	print type + ' ' + id
	cookie['type'] = type
	cookie['type']['expires']= 7*24*60*60
	cookie['id'] = id
	cookie['id']['expires']= 7*24*60*60

def clear_cookies():
	cookie.load(os.environ.get('HTTP_COOKIE'))
	cookie['id'] = ''
	cookie['id']['expires']='Thu, 01 Jan 1970 00:00:00 GMT'
	cookie['type'] = ''
	cookie['type']['expires']='Thu, 01 Jan 1970 00:00:00 GMT'

def print_cookie():
	print cookie

def return_cookie():
	return cookie
	
posted_data = cgi.FieldStorage()
if('cmd' in posted_data):
	print """Content-type: text/html\n\n

	<html><body>"""
	if(posted_data['cmd'].value == "set"):
		id = posted_data['id'].value
		type = posted_data['type'].value
		set_session(type,id)
	elif(posted_data['cmd'].value == 'clear'):
		clear_cookies()
	
	print "</body></html>"