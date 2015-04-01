#!python
# -*- coding: UTF-8 -*-

import cgi
import json
# enable debugging
import cgitb
cgitb.enable()

store = cgi.FieldStorage()
data = json.load(open("klebsiella-pneumoniae_ti.fa.filtered.genomes.innate_resistance.json"))


options = {
    "genome_ids": data.keys(),
    "dataset_ids": data.values()[0].keys()
}


print "Content-Type: application/json;charset=utf-8;"
print

print json.dumps(options)
