#!python
# -*- coding: UTF-8 -*-

import json
# enable debugging
import cgitb
cgitb.enable()

print "Content-Type: application/json;charset=utf-8;"
print

print json.dumps({
        "information": 5
    })
