#!/usr/bin/python

import Cookie
import os

def retrieve_current_session():
	c = Cookie.SimpleCookie();
	if 'HTTP_COOKIE' in os.environ:
		c.load(os.environ.get('HTTP_COOKIE')
	return c

def set_session(id, type):
	c = retrieve_current_session()
	c['id']=id
	c['type']=type 

def get_session():
	c = retrieve_current_session()
	current_session=dict()
	current_session['id'] = c['id']
	current_session['type'] = c['type']
	return current_session
	
def clear_session():
	c = retrieve_current_session()
	c['id'] = ''
	c['type'] = ''
	c['id']['expires']='Thu, 01 Jan 1970 00:00:00 GMT'
	c['type']['expires']='Thu, 01 Jan 1970 00:00:00 GMT'

def is_set():
	c = retrieve_current_session()
	if(c['id'] and c['type']):
		return 1
	else:
		return 0

def print_session():
	c = retrieve_current_session()
	print c
