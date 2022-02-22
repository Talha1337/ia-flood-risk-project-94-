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
#for x in stations_highest_rel_level_noname(stations, 5):
    #plot_water_level_with_fit(x[0], datetime.timedelta(2), x[0].typical_range, 4)
t = [datetime.datetime(2016, 12, 30), datetime.datetime(2016, 12, 31), datetime.datetime(2017, 1, 1),
     datetime.datetime(2017, 1, 2), datetime.datetime(2017, 1, 3), datetime.datetime(2017, 1, 4),
     datetime.datetime(2017, 1, 5)]
print(polyfit(t, [59, 58, 49, 658, 6589, 8585, 8686], 3))