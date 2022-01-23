# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from haversine import haversine, Unit
from .utils import sorted_by_key
def stations_by_distance(stations,p):
    distancelist = []
    for station in stations:
        stationandlist = (station.name, haversine(station.coord, p))
        distancelist.append(stationandlist)
    return sorted_by_key(distancelist, 1)
