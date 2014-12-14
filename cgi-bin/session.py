#!/usr/bin/python

import shelve
import os
import string

def retrieve_current_session():
	c = Cookie.SimpleCookie()
	if 'HTTP_COOKIE' in os.environ:
		c.load(os.environ.get('HTTP_COOKIE'))
	return c

def generate_key():
	return ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(10)])

def create_session(id, type):
	sessions = shelve.open('shelve.db')
	c = dict()
	c['id']=id
	c['type']=type
	key = generate_key()
	sessions[key] = c
	return 

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
	if('id' in c and 'type' in c):
		print 'What?</br>'
		return 1
	else:
		print 'Why?</br>'
		return 0

def print_session():
	c = retrieve_current_session()
	print c
