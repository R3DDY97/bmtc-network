#!/usr/bin/env python

import os
from flask import (Flask, render_template, request)
from webbrowser import open_new_tab
from .web_form import SearchForm

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    form = SearchForm()
    if request.method == 'POST' and form.validate():
        origin, destination = [request.form[i]
                               for i in ["origin", "destination"]]
        print(origin, destination)
    return render_template("search.html", form=form)


@app.route("/bmtc_map")
def bmtc_map():
    open_new_tab("./templates/bstops_map/index.html")
    return render_template("index.html")


@app.route("/network")
def network():
    return render_template("bmtc_map.html")


@app.route("/stats")
def stats():
    return render_template("stats.html")
