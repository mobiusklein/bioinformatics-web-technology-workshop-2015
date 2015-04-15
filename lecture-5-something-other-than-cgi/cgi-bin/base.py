#!python
# -*- coding: UTF-8 -*-
import matplotlib
matplotlib.use("svg")
from matplotlib import pyplot as plt
import cgi
import cgitb
import spectra
cgitb.enable()

params = cgi.FieldStorage()

db = spectra.MSMSSqlDB("spectra.db")

observed_precursor_count = db.execute("select count(*) from ObservedPrecursorSpectrum;").next()[0]
default_value = 866

observed_precursor = db.precursor_type.from_sql((db.execute("select * from ObservedPrecursorSpectrum\
 where precursor_id={0};".format(params.getvalue("spectra_id", default_value))).next()), db)

page_buffer = open("base.html").read()

spectra.plot_observed_spectra(observed_precursor.tandem_data, title="Tandem Spectra Observed")
fig = plt.gcf()
fig.set_figheight(7.5)
fig.set_figwidth(10.5)
plt.savefig("tandem_spectra.svg")

print "Content-Type: text/html;charset=utf-8;"
print

print page_buffer.format(precursor=observed_precursor,
                         observed_precursor_count=observed_precursor_count,
                         number_of_scans=len(observed_precursor.scans),
                         number_of_tandem_spectra=len(observed_precursor.tandem_data),
                         tandem_table="",
                         img_path="tandem_spectra.svg")
