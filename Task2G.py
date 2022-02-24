from floodsystem.analysis import plot_water_level_with_fit
from floodsystem.analysis import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level_noname
from floodsystem.stationdata import update_water_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.flood import stations_level_over_threshold
from floodsystem.analysis import polyfit
from floodsystem.station import MonitoringStation
import numpy as np
import math
import floodsystem
import datetime


from floodsystem.analysis import plot_water_level_with_fit
from floodsystem.analysis import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level_noname
from floodsystem.stationdata import update_water_levels
from floodsystem.analysis import polyfit
import matplotlib.pyplot as plt
import matplotlib as pt
import datetime

stations = build_station_list()
update_water_levels(stations)
severe_risk = []
high_risk = []
moderate_risk = []
low_risk = []

"""
for station in stations:
    if station.relative_water_level < 1.0:
        low_risk.append(x[0])
    if station.relative_water_level < 2.0:
        moderate_risk.append(x[0])
    if station.relative_water_level < 3.0:
        high_risk.append(x[0])
    else:
        severe_risk.append(x[0])
 
for station in station:



    for x in stations_highest_rel_level(stations, len(stations)):
        if x[1] < 1.0:
            low_risk.append(x[0])
        if x[1] < 2.0:
            moderate_risk.append(x[0])
        if x[1] < 3.0:
            high_risk.append(x[0])
        else:
            severe_risk.append(x[0])
"""

t = [datetime.datetime(2016, 12, 30), datetime.datetime(2016, 12, 31), datetime.datetime(2017, 1, 1),
     datetime.datetime(2017, 1, 2), datetime.datetime(2017, 1, 3), datetime.datetime(2017, 1, 4),
     datetime.datetime(2017, 1, 5)]
for x in stations_highest_rel_level_noname(stations, len(stations)):
    leveldata = fetch_measure_levels(x[0].measure_id, datetime.timedelta(2))
    num2datelist = []
    for x in leveldata[0]:
        num2datelist.append(pt.dates.date2num(x))
    x = np.array(num2datelist)
    y = leveldata[1]
    p_coeff = np.polyfit(x - x[0] , y, 3)
    poly = np.poly1d(p_coeff)




print("\n Low risk:\n")
print(low_risk)
print("\n moderate risk:\n")
print(moderate_risk)
print("\n High risk:\n")
print(high_risk)
print("\n Severe risk: \n")
print(severe_risk)