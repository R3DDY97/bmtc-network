#!/usr/bin/env python

from flask import (Flask, render_template, request)
from webbrowser import open_new_tab
from .web_form import SearchForm
from .bmtc_utils import TripPlanner

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    form = SearchForm()
    if request.method == 'POST' and form.validate():
        origin, destination = [request.form[i].strip()
                               for i in ["origin", "destination"]]
        # print(origin, destination)
        # if not origin or not destination:
        #     error = "Need to enter both bustops to search"
        #     return render_template("search.html", error=error)

        trip = TripPlanner(origin, destination)
        trip_details = trip.trip_details()

        if None in trip_details:
            error = "ERR0R Couldnt find the bus stop {}".format(
                trip_details[1])
            return render_template("search.html", error=error)

        direct_header = ["Bus", "stops", "Bus stops in between"]
        indirect__header = ["Bus No", "Get Down Here", "Second Bus"]

        if "direct" in trip_details:
            trip_details = trip_details["direct"]
            return render_template("search.html",
                                   origin=origin, destination=destination,
                                   items=trip_details, header=direct_header)
        return render_template("indirect_search.html",
                               origin=origin, destination=destination,
                               items=trip_details, header=indirect__header)
    return render_template("search.html", form=form)


@app.route("/bmtc_map")
def bmtc_map():
    open_new_tab("./templates/qgis2web/index.html")
    return render_template("index.html")


@app.route("/network")
def network():
    return render_template("index.html")


@app.route("/stats")
def stats():
    return render_template("index.html")
