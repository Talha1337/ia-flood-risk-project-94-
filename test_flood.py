from distutils.command.build import build
from multiprocessing import dummy
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.geo import *
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold
from floodsystem.flood import stations_highest_rel_level

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list

stations = build_station_list()
update_water_levels(stations)

def test_stations_level_over_threshold():
    for x in stations_level_over_threshold(stations, 0.5):
        assert x[1] > 0.5
    for x in range(len(stations_level_over_threshold(stations, 0.5))-1):
        assert stations_level_over_threshold(stations, 0.5)[x][1] >= stations_level_over_threshold(stations, 0.5)[x+1][1]

def test_stations_highest_rel_level():
    for x in range(9):
        assert stations_highest_rel_level(stations, 10)[x][1] >= stations_highest_rel_level(stations, 10)[x+1][1]
