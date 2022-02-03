from distutils.command.build import build
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.geo import *
from floodsystem.station import inconsistent_typical_range_stations

def test_stations_by_distance():
    stations = build_station_list()
    for x in stations_by_distance(stations, (52.2053, 0.1218))[0:10]:
        assert x[1] < 20
    for x in stations_by_distance(stations, (52.2053, 0.1218))[-11:-1]:
        assert x[1] > 100
def test_stations_within_radius():
    stations = build_station_list()
    assert stations_within_radius(stations, (52.2053, 0.1218), 0) == [] #empty list, no station can be directly on top of this point
    assert len(stations_within_radius(stations, (52.2053, 0.1218), 1000000)) > 0 # this should encompass every station in the whole station database
def test_rivers_with_station():
    stations = build_station_list()
    rivernames = rivers_with_station(stations)
    x = sorted(list(rivernames))
    assert len(x) > 0 #river names are included
    assert sorted(x) == x #river names are alphabetical
def test_stations_by_river():
    stations = build_station_list()
    assert len(stations_by_river(stations)) > 0 #there are more than 0 rivers with stations
def test_rivers_by_station_number():
    stations = build_station_list()
    assert len(rivers_by_station_number(stations, 10)) == 11
    assert (rivers_by_station_number(stations,10))[0][1] > (rivers_by_station_number(stations,10))[1][1]

"""Task 1E"""
def test_rivers_by_station_number():
    """Build a list of stations"""
    stations = build_station_list()
    """Test to see if the function can be called"""
    rivers_by_station_number(stations, 10)