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


page_buffer = '''
<!DOCTYPE html5>
<html>
<head>
    <title>Yet Another Databases Example</title>
    <link rel="stylesheet" type="text/css" href="/assets/style.css">
</head>
<body>
<h2>Observed Spectrum Database</h2>
<div style='float: left;'>
<p>
    There are {observed_precursor_count} precursor spectra in this database.
</p>
<div>
    <b>Current selected precursor spectrum:</b> {precursor.id}
    <table id='precursor-stats'>
        <tr>
            <td>Neutral Mass</td>
            <td>{precursor.neutral_mass}</td>
        </tr>
        <tr>
            <td>Charge</td>
            <td>{precursor.charge}</td>
        </tr>
        <tr>
            <td>Number of scans</td>
            <td>{number_of_scans}</td>
        </tr>
        <tr>
            <td>Number of tandem spectra</td>
            <td>{number_of_tandem_spectra}</td>
        </tr>
    </table>
</div>
<h4>Tandem Spectra</h4>
<table id='tandem-table'>
<tr><th>Neutral Mass</th><th>Intensity</th><th>Charge</th></tr>
{tandem_table}
</table>
</div>
<div style='float: left;margin-left:15px;'>
<h3>Tandem Spectra Graph</h3>
<object data="../{img_path}" type="image/svg+xml">
</object>
</div>
</body>
</html>
'''

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
