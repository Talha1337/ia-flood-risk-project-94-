from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number
from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations
stations = build_station_list()

list_of_inconsistent_stations = inconsistent_typical_range_stations(stations)
inconsistent = []
for station in list_of_inconsistent_stations:
    inconsistent.append(station.name)

inconsistent.sort()
print(inconsistent)