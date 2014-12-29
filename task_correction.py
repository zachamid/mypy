#!/usr/bin/python

import cgi, cgitb
import os
import json
import MySQLdb
import MySQLdb.cursors
import db_connection
import xml
import read
import task_delivery
cgitb.enable()

def judge_correctness(id, code):
	print exec(code)
	print exec(get_python_code_from_file(id, 'task_complete.py'))

def judge_similarity():

def judge_time():

def judge_attempts():