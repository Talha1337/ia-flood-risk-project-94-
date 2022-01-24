# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from haversine import haversine, Unit
from .utils import sorted_by_key
def stations_by_distance(stations,p):
    distancelist = [] #forms empty list of stations and their respective distances
    for station in stations:
        stationandlist = (station.name, haversine(station.coord, p)) #tuple formed, ([name of station], [distance between station coordinates and p])
        distancelist.append(stationandlist) 
    return sorted_by_key(distancelist, 1) #stations/distances returned, sorted by entry 1 in the tuple (distance), distancelist returned in ascending order

def stations_within_radius(stations, centre, r):
    namelist = []
    distancelist = stations_by_distance(stations, centre) #list of stations/distances made, entry [1] in each tuple is distance
    disttemplate = distancelist.copy() #to ensure that the loop goes through each index
    for x in disttemplate:
        if x[1] < r:
            pass
        else:
            distancelist.remove(x) #remove stations / distances that are more than the maximum distance allowed
    sortedlist = sorted_by_key(distancelist, 0) #sorts this list
    for y in sortedlist:
        namelist.append(y[0])
    return namelist #namelist formed from taking each station, entry 0 in the tuple, and appending them to form a list of station names.

def rivers_with_station(stations):
    rivers = set() #prevents duplicates
    for station in stations:
        rivers.add(station.river) #added associated rivers to each station
    return rivers

def stations_by_river(stations):
    river2station = dict() #empty dictionary
    river_list = rivers_with_station(stations) #river names list produced
    for rivername in river_list: #going through each river name
        commonriver = [] # empty list made empty for each time code goes through loop, for common rivers
        for station in stations:
            if station.river == rivername:
                commonriver.append(station.name) #consider each station each time, and if the river name matches the rivername in river_list, it is appended to commonriver
        river2station[rivername] = commonriver #add the list formed for commonriver into the dictionary
    return river2station #returns completed dictionary

"""Task 1E"""
def rivers_by_station_number(stations, N):
    """Empty list to be filled with stations"""
    river_list = stations_by_river(stations)
    """creating tuples of rivers and number of stations"""
    river_stationnumber_list = []
    for river in river_list:
        len(river)
        x = (river, len(river))
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