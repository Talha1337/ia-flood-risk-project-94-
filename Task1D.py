from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list
stations = build_station_list()
rivernames = rivers_with_station(stations)
x = sorted(list(rivernames))
print(str(len(rivernames)) + " rivers with at least one station, first 10 alphabetically: " + str(x[0:10]))

print(sorted(stations_by_river(stations)["River Aire"]))
print(sorted(stations_by_river(stations)["River Cam"]))
print(sorted(stations_by_river(stations)["River Thames"]))