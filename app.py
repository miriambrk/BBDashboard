from flask import Flask, render_template, jsonify, redirect

import os

from bb_functions import get_sample_names, get_sample_metadata, get_OTU_desc, get_sample_values
#, get_washing_freq

app = Flask(__name__)

#read all the belly button data files and store in JSON structures
sample_names, samples_df = get_sample_names()
otu_data = get_OTU_desc()
meta_data = get_sample_metadata()

# display dashboard homepage
@app.route("/")
def index():
    return render_template("index.html")

#return list of sample names
@app.route("/names")
def names():
    return (jsonify(sample_names))

#returning list of OTU descriptions
@app.route("/otu")
def otu():
    return (jsonify(otu_data))

#get json dictionary of sample metadata
@app.route("/metadata/<sample>")
def metadata(sample):
    print(meta_data[int(sample)])
    return (jsonify(meta_data[int(sample)]))

#get Weekly Washing Frequency as a number.
@app.route("/wfreq/<sample>")
def wfreq(sample):
    wfreq = meta_data[int(sample)]['WFREQ']
    return (jsonify(wfreq))

#get Sample Values and related OTU IDs for a given sample
@app.route("/samples/<sample>")
def samples(sample):
    sample_data = get_sample_values(sample)
    return (jsonify(sample_data))


if __name__ == "__main__":
    app.run(debug=True)
