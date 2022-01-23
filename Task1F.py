from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number
#from floodsystem.station import 

stations = build_station_list()
rivernames = rivers_with_station(stations)
stations = build_station_list()


print(stations[4].typical_range)


print(stations[4].typical_range_consistent())