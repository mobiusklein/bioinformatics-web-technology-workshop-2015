#!python

import cgi
# enable debugging
import cgitb
import json
cgitb.enable()

store = cgi.FieldStorage()
data = json.load(open("klebsiella-pneumoniae_ti.fa.filtered.genomes.innate_resistance.json"))

parameters = {}
for key in store.keys():
    parameters[key] = store[key].value

if parameters.get("genome_id") is None:
    parameters["genome_id"] = u'573'
if parameters.get("dataset_id") is None:
    parameters["dataset_id"] = "comprehensive_antibiotic_resistance_database_AT-polypeptides"

genome = data[parameters["genome_id"]]
dataset = genome[parameters["dataset_id"]]


print "Content-Type: application/json;charset=utf-8;"
print

print json.dumps(dataset)
