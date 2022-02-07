"""importing functions that might be used"""
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number
stations = build_station_list() #list of stations generated
rivernames = rivers_with_station(stations)

print("*** Task 1E: CUED Part IA Flood Warning System ***")
"""Print out the 9 rivers with the most stations"""
print(rivers_by_station_number(stations, 9)) 
