#!/usr/bin/python

import Cookie
import os
import string

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
	cookie['type'] = type
	cookie['type']['expires']= 7*24*60*60
	cookie['id'] = id
	cookie['id']['expires']= 7*24*60*60

def clear_cookies():
	cookie['type']['expires']='Thu, 01 Jan 1970 00:00:00 GMT'
	cookie['id']['expires']='Thu, 01 Jan 1970 00:00:00 GMT'

def print_cookie():
	print cookie

def return_cookie():
	return cookie