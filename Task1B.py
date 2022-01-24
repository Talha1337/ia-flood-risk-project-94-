from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
stations = build_station_list() 
#list of stations generated
print(stations_by_distance(stations, (52.2053, 0.1218))[0:10])
#1st (0) to 10th (10) station, taking the stations closest in distance
print(stations_by_distance(stations, (52.2053, 0.1218))[-11:-1])
#10th to last (-11) to last (-1) station, taking the stations now furthest in distance
for x in stations_by_distance(stations, (52.2053, 0.1218))[0:10]:
    assert x[1] < 20
for x in stations_by_distance(stations, (52.2053, 0.1218))[-11:-1]:
    assert x[1] > 100
