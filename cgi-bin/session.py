#!/usr/bin/python

import Cookie
import os

c = Cookie.SimpleCookie();
if 'HTTP_COOKIE' in os.environ:
	c.load(os.environ.get('HTTP_COOKIE')

def set_session(id, type):
	c['id']=id
	c['type']=type 

def get_session():
	current_session=dict()
	current_session['id'] = c['id']
	current_session['type'] = c['type']
	return current_session
	
def clear_session():
	c['id'] = ''
	c['type'] = ''
	c['id']['expires']='Thu, 01 Jan 1970 00:00:00 GMT'
	c['type']['expires']='Thu, 01 Jan 1970 00:00:00 GMT'

def is_set():
	if(c['id'] and c['type']):
		return 1
	else:
		return 0

def print_session():
	print c
