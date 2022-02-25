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

"""
"""
def linear_regression(station, dates):
    try:
        leveldata = fetch_measure_levels(station.measure_id, datetime.timedelta(days = dates))
    except:
        return False
    num2datelist = [] 
    for x in leveldata[0]:
        num2datelist.append(pt.dates.date2num(x))
    if num2datelist == []:
        return False 
    x = np.array(num2datelist - num2datelist[-1]) 
    y = np.array(leveldata[1])
    p_coeff = np.polyfit(x, y, 1)
    if p_coeff[0] >= 0:
        return True
    else:
        return False"""

         
#if levels_and_dates[1][0] > levels_and_dates[1][-1]:
#continue


counter = 0
for x in stations_highest_rel_level_noname(stations, len(stations)):

    if x[1] < 1.0: #and x[0] not in moderate_risk and not in high_risk and not in severe_risk:
        low_risk.append(x[0].town)
    elif x[1] < 2.0: #and x[0] not in high_risk or severe_risk:
        moderate_risk.append(x[0].town)
    elif x[1] < 3.0: #and x[0] not in severe_risk:
        high_risk.append(x[0].town)
    else:
        severe_risk.append(x[0].town)


severe_risk_set = set(severe_risk)
high_risk_set = set(high_risk)
moderate_risk_set = set(moderate_risk)
low_risk_set = set(low_risk)

for x in severe_risk_set:
    if x in high_risk_set:
        high_risk_set.remove(x)
    if x in moderate_risk_set:
        moderate_risk_set.remove(x)
    if x in low_risk_set:
        low_risk_set.remove(x)

for x in high_risk_set:
    if x in moderate_risk_set:
        moderate_risk_set.remove(x)
    if x in low_risk_set:
        low_risk_set.remove(x)

for x in moderate_risk_set:
    if x in low_risk_set:
        low_risk_set.remove(x)

if None in severe_risk_set:
    severe_risk_set.remove(None)
    
if None in high_risk_set:
    high_risk_set.remove(None)
    
if None in moderate_risk_set:
    moderate_risk_set.remove(None)
    
if None in low_risk_set:
    low_risk_set.remove(None)


print("\n Low risk:\n")
print(set(low_risk_set))
print("\n moderate risk:\n")
print(set(moderate_risk_set))
print("\n High risk:\n")
print(set(high_risk_set))
print("\n Severe risk: \n")
print(set(severe_risk_set))
print(len(list(low_risk_set)))

"""

t = [datetime.datetime(2016, 12, 30), datetime.datetime(2016, 12, 31), datetime.datetime(2017, 1, 1),
     datetime.datetime(2017, 1, 2), datetime.datetime(2017, 1, 3), datetime.datetime(2017, 1, 4),
     datetime.datetime(2017, 1, 5)]
"""
"""
for x in stations_highest_rel_level_noname(stations, len(stations)):
    leveldata = fetch_measure_levels(x[0].measure_id, datetime.timedelta(2))
    num2datelist = []
    for x in leveldata[0]:
        num2datelist.append(pt.dates.date2num(x))
    x = np.array(num2datelist)
    y = leveldata[1]
    p_coeff = np.polyfit(x - x[0] , y, 3)
    poly = np.poly1d(p_coeff)
"""
"""
counter  =0
for x in stations_highest_rel_level_noname(stations, len(stations)):
    dates, levels = fetch_measure_levels( x[0].measure_id, datetime.timedelta(2))
    if x[0].measure_id == None:
        pass
    elif levels[0] > levels[1]:
        counter += 1
        print(counter)


print("\n Low risk:\n")
print(set(low_risk))
print("\n moderate risk:\n")
print(set(moderate_risk))
print("\n High risk:\n")
print(set(high_risk))
print("\n Severe risk: \n")
print(set(severe_risk))

"""