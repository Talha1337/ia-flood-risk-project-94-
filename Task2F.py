from floodsystem.analysis import plot_water_level_with_fit
from floodsystem.analysis import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level_noname
from floodsystem.stationdata import update_water_levels
import datetime
stations = build_station_list()
update_water_levels(stations)
for x in stations_highest_rel_level_noname(stations, 5):
    plot_water_level_with_fit(x[0], datetime.timedelta(2), x[0].typical_range, 4)