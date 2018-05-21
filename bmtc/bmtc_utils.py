#!/usr/bin/env python3

import json


class TripPlanner:

    def __init__(self, origin, destination):
        self.origin, self.destination = origin, destination

    def trip_details(self):

        self.route_bstops = load_json("data/new_route_bstops.json")
        self.bstop_routes = load_json("data/new_bstop_routes.json")
        # self.route_bstops = load_json("data/api_route_stops.json")
        # self.bstop_routes = load_json("data/api_bstop_routes.json")

        try:

            self.origin_routes, self.dest_routes = self.bstop_routes[
                self.origin], self.bstop_routes[self.destination]
        except KeyError as err:
            return None, str(err)

        self.comn_routes, self.origin_uncomn_routes = [], []

        for route in self.origin_routes:
            if route in self.dest_routes:
                self.comn_routes.append(route)
            else:
                self.origin_uncomn_routes.append(route)
        self.dest_uncomn_routes = [
            r for r in self.dest_routes if r not in self.comn_routes]

        if self.comn_routes:
            direct_list = []
            for croute in self.comn_routes:
                try:
                    cr_stops = self.route_bstops[croute]
                    origin_index = cr_stops.index(self.origin)
                    dest_index = cr_stops.index(self.destination)
                    diff = abs(origin_index - dest_index)
                    if origin_index < dest_index:
                        btwn_stops = cr_stops[origin_index:dest_index]
                    else:
                        btwn_stops = cr_stops[dest_index:origin_index+1][::-1]
                    direct_list.append([croute, diff, btwn_stops])
                except ValueError:
                    pass
            return {"direct": sorted(direct_list, key=lambda item: item[1])}
        else:
            return sorted(self.indirect_trip(), key=lambda item: item[-1])

    def indirect_trip(self):
        indirect_routes = []
        for route in self.origin_uncomn_routes:
            indirect_route = self.find_destination(route)
            if indirect_route:
                indirect_routes.append(indirect_route)
        return indirect_routes

    def find_destination(self, route):
        for bstop in self.route_bstops[route]:
            for iroute in self.bstop_routes[bstop]:
                if self.destination in self.route_bstops[iroute]:
                    try:

                        ucr_stops = self.route_bstops[route]
                        midr_stops = self.route_bstops[iroute]

                        origin_index = ucr_stops.index(self.origin)
                        midstop_index1 = ucr_stops.index(bstop)
                        midstop_index2 = midr_stops.index(bstop)
                        dest_index = midr_stops.index(self.destination)
                        diff1 = abs(origin_index - midstop_index1)
                        diff2 = abs(midstop_index2 - dest_index)
                        return route, diff1, bstop, diff2, iroute, diff1+diff2
                    except ValueError:
                        pass
        return None


def broute_info(route_no=None, bstop=None):
    route_bstops = load_json("data/new_route_bstops.json")
    if route_no:
        details = route_bstops.get(route_no, None)
    if details:
        details = [(num, i) for num, i in enumerate(details, 1)]
        return details


def bstop_info(bstop):
    bstop_routes = load_json("data/new_bstop_routes.json")
    if bstop:
        details = bstop_routes.get(bstop, None)
    if details:
        details = [(num, i) for num, i in enumerate(details, 1)]
        return details
    return None


def load_json(json_file):
    with open(json_file, "r+") as rfile:
        py_obj = json.load(rfile)
    return py_obj


def kia_route_info(kia_route):
    kroute_stops = load_json("data/kia_route_stops.json")
    if kia_route:
        details = kroute_stops.get(kia_route, None)

    if details:
        details = [(num, i) for num, i in enumerate(details, 1)]
        return details
    return None


def kia_stop_info(kia_stop):
    kstop_routes = load_json("data/kia_stop_routes.json")
    if kia_stop:
        details = kstop_routes.get(kia_stop, None)

    if details:
        details = [(num, i) for num, i in enumerate(details, 1)]
        return details
    return None
