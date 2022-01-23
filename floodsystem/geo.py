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
def stations_within_radius(stations, centre, r):
    namelist = []
    distancelist = stations_by_distance(stations, centre)
    disttemplate = distancelist.copy()
    for x in disttemplate:
        if x[1] < r:
            pass
        else:
            distancelist.remove(x)
    sortedlist = sorted_by_key(distancelist, 0)
    for y in sortedlist:
        namelist.append(y[0])
    return namelist