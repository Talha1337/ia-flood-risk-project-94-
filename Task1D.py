from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list
stations = build_station_list()
rivernames = rivers_with_station(stations)
x = sorted(list(rivernames)) #Rivers now sorted alphabetically
print(str(len(rivernames)) + " rivers with at least one station, first 10 alphabetically: " + str(x[0:10])) # first 10 alphabetical rivers

print(sorted(stations_by_river(stations)["River Aire"])) #stations ordered alphabetically for each river
print(sorted(stations_by_river(stations)["River Cam"]))
print(sorted(stations_by_river(stations)["River Thames"]))

assert len(x) > 0 #river names are included
assert sorted(x) == x #river names are alphabetical
assert len(stations_by_river(stations)) > 0 #there are more than 0 rivers with stations