from floodsystem.analysis import plot_water_level_with_fit
from floodsystem.analysis import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level_noname
from floodsystem.stationdata import update_water_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.flood import stations_level_over_threshold
from floodsystem.analysis import polyfit
import floodsystem
import datetime

stations = build_station_list()
update_water_levels(stations)
severe_risk = []
high_risk = []
moderate_risk = []
low_risk = []

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


print("\n Low risk:\n")
print(low_risk)
print("\n moderate risk:\n")
print(moderate_risk)
print("\n High risk:\n")
print(high_risk)
print("\n Severe risk: \n")
print(severe_risk)