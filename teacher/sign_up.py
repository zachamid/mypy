#!/usr/bin/env python

import Cookie, cgi, cgitb, os,sys
sys.path.append(os.pardir)
import common_components
from mako.template import Template
from mako.lookup import TemplateLookup

cgitb.enable()

cookies = Cookie.SimpleCookie(os.environ.get("HTTP_COOKIE",""))
html_header = ''
if cookies.has_key('id') and cookies.has_key('type'):
	html_header += cookies
	if cookies['type'].value == 'Student':
		html_header += '\nLocation:../index.py'
	else:
		html_header += '\nLocation:index.py'

include_lookup = TemplateLookup(directories=['/var/www/thirdyearproject/teacher/templates'])
template_file = open('sign_up_template.html')
page_template = Template(template_file.read(), lookup=include_lookup)
print page_template.render(html_header=html_header)