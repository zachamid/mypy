#!/usr/bin/python

from splinter import Browser

browser = Browser('zope.testbrowser')
url = 'http://webvm.cs.man.ac.uk/'
sites = ['correction_page.py','league_table.py','playground.py','sign_up.py','task_list.py','task_page.py','user_page.py']

for site in sites:
	browser.visit(url+site)
	print browser.url