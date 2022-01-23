from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number
from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations
stations = build_station_list()

"""collect all inconsistent stations into a list"""
list_of_inconsistent_stations = inconsistent_typical_range_stations(stations)
"""creating an empty list to fill"""
inconsistent = []
"""Filling the list with the names of the inconsistent stations"""
for station in list_of_inconsistent_stations:
    inconsistent.append(station.name)

"""sort the list into alphabetical order"""
inconsistent.sort()
print(inconsistent)