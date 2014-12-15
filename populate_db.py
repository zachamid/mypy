#!/usr/bin/python

import MySQLdb
import sys

db = MySQLdb.connect('localhost','root','S0crat3s34!','test');
cursor = db.cursor()
