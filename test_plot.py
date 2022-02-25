
from floodsystem.datafetcher import fetch_measure_levels
import datetime
from floodsystem.plot import plot_water_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list

stations = build_station_list()

def test_plot_water_levels():
    assert plot_water_levels(stations[0], 2, stations[0].typical_range)

def test_plot_water_level_with_fit():
    assert plot_water_level_with_fit(stations[0], 2, stations[0].typical_range, 3)