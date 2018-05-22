#!/usr/bin/env python3

from flask import (Flask, render_template, request)
from .bmtc_utils import (TripPlanner, broute_info,
                         bstop_info, kia_route_info, kia_stop_info)
from .web_form import (SearchForm, RouteForm,
                       BstopForm, KstopForm, KrouteForm)

app = Flask(__name__)


# @app.route("/")
# def index():
#     return render_template("index.html")


@app.route("/", methods=["GET", "POST"])
def search():
    form = SearchForm()
    if request.method == 'POST' and form.validate():
        origin, destination = [request.form[i].strip()
                               for i in ["origin", "destination"]]

        trip = TripPlanner(origin, destination)
        trip_details = trip.trip_details()

        if None in trip_details:
            error = "ERR0R Couldnt find the bus stop {}\n".format(
                trip_details[1])
            return render_template("search.html", error=error)

        direct_header = ["Bus", "stops", "Bus stops in between"]
        indirect__header = ["Bus No", "stops",
                            "Get Down Here", "stops", "Second Bus", "total"]
        caption = "Trip Details from {} to {}\n".format(origin, destination)
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
        hdr = ["sl", "Bus Stops"]
        route_details = broute_info(route_no)
        if route_details:
            caption = "{} Bus stops for the route {}\n".format(
                len(route_details), route_no)
            return render_template("route.html", header=hdr, items=route_details, caption=caption)
    return render_template("route.html", form=form)


@app.route("/bmtc_map")
def bmtc_map():
    return render_template("map.html")


@app.route("/kia_stop", methods=["GET", "POST"])
def kia_stop():
    form = KstopForm()
    if request.method == 'POST' and form.validate():
        kia_stop = request.form["kia_stop"].strip()
        print(kia_stop)
        details = kia_stop_info(kia_stop)
        if details:
            hdr = ["sl", "Bus Stops"]
            caption = "{} KIA routes for the bus stop {}\n".format(
                len(details), kia_stop)
            return render_template("kia_stop.html", header=hdr, items=details, caption=caption)
    return render_template("kia_stop.html", form=form)


@app.route("/bstop", methods=["GET", "POST"])
def bstop():
    form = BstopForm()
    if request.method == 'POST' and form.validate():
        bstop = request.form["bstop"].strip()
        print(bstop)
        details = bstop_info(bstop)
        if details:
            hdr = ["sl", "Bus Routes"]
            caption = "{} routes available  for the bus stop {}\n".format(
                len(details), bstop)
            return render_template("bstop.html", header=hdr, items=details, caption=caption)
    return render_template("bstop.html", form=form)


@app.route("/kia_route", methods=["GET", "POST"])
def kia_route():
    form = KrouteForm()

    if request.method == 'POST' and form.validate():
        kia_route = request.form["kia_route"].strip()
        print(kia_route)
        details = kia_route_info(kia_route)
        if details:
            hdr = ["sl", "Bus Stops"]
            caption = "{} Bus stops for the KIA route {}\n".format(
                len(details), kia_route)
            return render_template("kia_route.html", header=hdr, items=details, caption=caption)
    return render_template("kia_route.html", form=form)
