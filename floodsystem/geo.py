# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from haversine import haversine, Unit
from .utils import sorted_by_key
def stations_by_distance(stations,p):
    """forms empty list of stations and their respective distances. 
    tuple formed, ([name of station], [distance between station coordinates and p]).
    stations/distances returned, sorted by entry 1 in the tuple (distance), distancelist returned in ascending order."""
    distancelist = [] 
    for station in stations:
        stationandlist = (station.name, haversine(station.coord, p)) 
        distancelist.append(stationandlist) 
    return sorted_by_key(distancelist, 1) 

def stations_within_radius(stations, centre, r):
    """list of stations/distances made, entry [1] in each tuple is distance
    template made so that loop is able to go through every index
    remove stations / distances that are more than the maximum distance allowed
    Finally, this sorts the stations alphabetically
    namelist formed from taking each station, entry 0 in the tuple, and appending them to form a list of station names."""
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
    """set made to prevent duplicates, river names added for each station to the set, set of rivers returned."""
    rivers = set()
    for station in stations:
        rivers.add(station.river) 
    return rivers

def stations_by_river(stations):
    """empty dictionary produced initially, list of river names produced, for each river name checking for common station,
    common river list produced for each river name the list goes through, and final list is appended to the empty dictionary."""
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
    """creating tuples of rivers and number of stations"""
    river_stationnumber_list = []
    for river in river_list:
        """Create a list of tuples containing the rivername and number of stations"""
        x = (river, len(river_list[river]))
        river_stationnumber_list.append(x)
    """sorting by number of stations"""
    ordered = sorted_by_key(river_stationnumber_list, 1, reverse=True)
    """Taking the first N terms"""
    Final_list = ordered[:N]
    """Checking the for additional rivers with the same number of stations as the Nth station"""
    for x in ordered[N:]:
        if x[1] == Final_list[N-1][1]:
            Final_list.append(x)
    return Final_list 