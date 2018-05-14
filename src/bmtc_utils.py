#!/usr/bin/env python3

import json


class TripPlanner:

    def __init__(self, origin, destination):
        self.origin, self.destination = origin, destination

    def trip_details(self):

        self.route_bstops = load_json("data/route_bstops.json")
        self.bstop_routes = load_json("data/bstop_routes.json")

        self.origin_routes, self.dest_routes = self.bstop_routes[
            self.origin], self.bstop_routes[self.destination]

        self.comn_routes, self.origin_uncomn_routes = [], []

        for route in self.origin_routes:
            if route in self.dest_routes:
                self.comn_routes.append(route)
            else:
                self.origin_uncomn_routes.append(route)
        self.dest_uncomn_routes = [
            r for r in self.dest_routes if r not in self.comn_routes]

        if self.comn_routes:
            direct_result_list = []
            for croute in self.comn_routes:
                try:
                    origin_index = self.route_bstops[croute].index(self.origin)
                    dest_index = self.route_bstops[croute].index(
                        self.destination)
                    diff = abs(origin_index - dest_index)
                    btwn_stops = self.route_bstops[croute][origin_index:
                                                           dest_index] or self.route_bstops[croute][dest_index:origin_index+1][::-1]
                    direct_result_list.append([diff, croute, btwn_stops])
                except ValueError:
                    pass
            return sorted(direct_result_list)
        else:
            return sorted(self.indirect_trip(), key=lambda item: item[1])

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
                    return route, bstop, iroute
        return None


def load_json(json_file):
    with open(json_file, "r+") as rfile:
        py_obj = json.load(rfile)
    return py_obj
