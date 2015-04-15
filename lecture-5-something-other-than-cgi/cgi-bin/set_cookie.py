#!python
# -*- coding: UTF-8 -*-
import cgi
import os
import cgitb
import json
cgitb.enable()

print "Content-type: text/html;"
print "Set-Cookie: myauth_cookie=true"
print
print "<a href='cookie_test.py'>Go Home</a>"
