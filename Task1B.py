from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
stations = build_station_list()
print(stations_by_distance(stations, (52.2053, 0.1218))[0:10])
print(stations_by_distance(stations, (52.2053, 0.1218))[-11:-1])