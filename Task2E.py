import matplotlib.pyplot as plt
from floodsystem.datafetcher import fetch_measure_levels
from datetime import datetime, timedelta
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level_noname
from floodsystem.plot import plot_water_levels

stations = build_station_list()
update_water_levels(stations)
x = stations_highest_rel_level_noname(stations,5) #acts in same way as stations_highest_rel_level but now it returns MonitoringStation objects rather than the station.name object.
stationlist = []
for station in x:
    stationlist.append(station[0]) #create a list of the stations
for station in stationlist:
    plot_water_levels(station, 10, station.typical_range) #


