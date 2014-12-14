#!/usr/bin/env python

import session, Cookie, cgi, cgitb, os

cgitb.enable()

string_cookie = os.environ.get('HTTP_COOKIE')

# If new session
if not session.in_session():
	session.set_session('Student', 0)
# If already existent session
else:
	cookie = session.return_cookie()
	cookie.load(string_cookie)

id = cookie['id'].value
type = cookie['type'].value
session.set_session(type, id+1)
	
session.print_cookie()
print 'Content-Type: text/html\n'
print '<html><body>'

if session.in_session:
   print type,'</br>',id

print '</body></html>'