import os
import csv
from flask import Flask, redirect

app = Flask(__name__)

tomb = 'https://www.lib.sfu.ca/help/publish/research-data-management/radar-retire'

reader = csv.reader(open('.data/link_redirect.csv'))
lookup = dict()
for row in reader:
    key = row[0]
    lookup[key] = row [1]

@app.route('/') #what route triggers function? this is root url.
def show_generic():
    return redirect(tomb, code = 404) #for base url, return generic tombstone

@app.route('/islandora/object/<pid>')
def rdm_moved(pid):
    try:
        new = lookup[pid]
        return redirect(new, code = 301) #return newlocation row where old = pid
    except:
        return redirect(tomb, code = 404)

@app.route('/pydio')
def pyd_redir():
    return redirect(tomb, code = 404)