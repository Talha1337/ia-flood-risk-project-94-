from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
stations = build_station_list()
update_water_levels(stations)
print(stations_highest_rel_level(stations,10)) #list of 10 stations with the highest level