from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
stations = build_station_list()
closestations = stations_within_radius(stations, (52.2053, 0.1218), 10) 
print(closestations)
assert stations_within_radius(stations, (52.2053, 0.1218), 0) == [] #empty list, no station can be directly on top of this point
assert len(stations_within_radius(stations, (52.2053, 0.1218), 1000000)) == 2165 # this should encompass every station in the whole station database