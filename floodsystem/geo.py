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

def rivers_with_station(stations):
    rivers = set()
    for station in stations:
        rivers.add(station.river)
    return rivers

def stations_by_river(stations):
    river2station = dict()
    river_list = rivers_with_station(stations)
    for rivername in river_list:
        commonriver = []
        for station in stations:
            if station.river == rivername:
                commonriver.append(station.name)
        river2station[rivername] = commonriver
    return river2station

"""Task 1E"""
def rivers_by_station_number(stations, N):
    """Empty list to be filled with stations"""
    river_list = stations_by_river(stations)
    river_stationnumber_list = []
    for river in river_list:
        len(river)
        x = (river, len(river))
        river_stationnumber_list.append(x)
    """sorting by n stations"""
    ordered = sorted_by_key(river_stationnumber_list, 1, reverse=True)
    Final_list = ordered[:N]
    for x in ordered[N:]:
        if x[1] == Final_list[N-1][1]:
            Final_list.append(x)
    return Final_list