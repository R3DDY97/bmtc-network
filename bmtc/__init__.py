#!/usr/bin/env python

from flask import (Flask, render_template, request)
# from webbrowser import open_new_tab
from .web_form import SearchForm, RouteForm
from .bmtc_utils import TripPlanner, broute_info

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

        trip = TripPlanner(origin, destination)
        trip_details = trip.trip_details()

        if None in trip_details:
            error = "ERR0R Couldnt find the bus stop {}".format(
                trip_details[1])
            return render_template("search.html", error=error)

        direct_header = ["Bus", "stops", "Bus stops in between"]
        indirect__header = ["Bus No", "stops",
                            "Get Down Here", "stops", "Second Bus", "total"]
        caption = "Trip Details from {} to {}".format(origin, destination)
        if "direct" in trip_details:
            trip_details = trip_details["direct"]
            return render_template("search.html", caption=caption,
                                   items=trip_details, header=direct_header)
        return render_template("indirect_search.html", caption=caption,
                               items=trip_details, header=indirect__header)
    return render_template("search.html", form=form)


@app.route("/route_info", methods=["GET", "POST"])
def route_info():
    form = RouteForm()
    if request.method == 'POST' and form.validate():
        route_no = request.form["route"].strip()
        print(route_no)
        route_details = broute_info(route_no)
        if route_details:
            caption = "{} Bus stops for the route {}".format(
                len(route_details), route_no)
            return render_template("route.html", items=route_details, caption=caption)
    return render_template("route.html", form=form)


@app.route("/bmtc_map")
def bmtc_map():
    try:
        # open_new_tab("./templates/qgis2web/index.html")
        return render_template("map.html")
    except:
        print("not opened map")

    return render_template("index.html")


@app.route("/network")
def network():
    return render_template("index.html")


@app.route("/stats")
def stats():
    return render_template("index.html")
