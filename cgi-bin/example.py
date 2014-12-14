#!/usr/bin/env python

import session, Cookie, cgi, cgitb, os

cgitb.enable()

string_cookie = os.environ.get('HTTP_COOKIE')
cookie = session.return_cookie()

# If new session
if not session.in_session():
	session.set_session('Student', 0)
# If already existent session
else:
	cookie.load(string_cookie)

id = cookie['id'].value
type = cookie['type'].value
session.set_session(type, int(id)+1)
	
session.print_cookie()
print """Content-type: text/html\n\n

<html><head><script src="/jquery-1.11.1.min.js"></script>
<script>
function clear_cookies(){
	var cookies = document.cookie.split(";");

    for (var i = 0; i < cookies.length; i++) {
    	var cookie = cookies[i];
    	var eqPos = cookie.indexOf("=");
    	var name = eqPos > -1 ? cookie.substr(0, eqPos) : cookie;
    	document.cookie = name + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT";
    	windows.location.reload();
    }
}
</script>
</head>"""
if session.in_session:
   print type,'</br>',id

print """\n
<button onclick="clear_cookies()"> Clear </button>"""