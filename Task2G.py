from floodsystem.analysis import plot_water_level_with_fit
from floodsystem.analysis import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level_noname
from floodsystem.stationdata import update_water_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.flood import stations_level_over_threshold
import floodsystem
import datetime

stations = build_station_list()
update_water_levels(stations)
severe_risk = []
high_risk = []
moderate_risk = []
low_risk = []
"""for station in stations:
    if """
for x in stations_highest_rel_level(stations, len(stations)):
    if x[1] <= 1.0:
        low_risk.append(x[0])

print(low_risk)