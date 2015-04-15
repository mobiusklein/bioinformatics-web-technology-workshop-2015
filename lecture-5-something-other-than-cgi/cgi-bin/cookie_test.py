#!python
# -*- coding: UTF-8 -*-
import cgi
import os
import cgitb
import json
cgitb.enable()

cookies = {pair.split("=", 1)[0]: pair.split("=", 1)[1] for pair in os.environ["HTTP_COOKIE"].split(";")}

if "myauth_cookie" in cookies:
    print "Content-type: text/html;"
    print
    print "Hello, friend"
else:
    print "Content-type: text/html"
    print
    print "I don't know you."

print "<br>"
print json.dumps(cookies, indent=2)
