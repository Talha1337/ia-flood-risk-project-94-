from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
stations = build_station_list() # Build list of stations
closestations = stations_within_radius(stations, (52.2053, 0.1218), 10) #finds the closest station within 10km of Cambridge City Centre
print(closestations)
