# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

    """Task 1F"""
    assert s.typical_range_consistent == True
    """Create stations with inconsistent data and then assert if they are false"""
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (2.3, -3.4445)
    river = "River X"
    town = "My Town"
    inconsistent_test_station_1 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    assert inconsistent_test_station_1.typical_range_consistent == False

    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = None
    river = "River X"
    town = "My Town"
    inconsistent_test_station_2 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    assert inconsistent_test_station_2.typical_range_consistent == False
    



"""Task 1F continued"""
def test_inconsistent_typical_range_stations():
    """Build a list of stations"""
    stations = build_station_list()
    """Test to see if the function can be called"""
    inconsistent_typical_range_stations(stations)
    dummystation = []
    """Test to see if the function can be called"""
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (2.5, -3.4445) #inconsistent
    river = "River X"
    town = "My Town"
    s1 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-3.4, -3.4445) #inconsistent
    river = "River Y"
    town = "My Town"
    s2 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = None #inconsistent
    river = "River X"
    town = "My Town"
    s3 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s4 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River Y"
    town = "My Town"
    s5 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    dummystation.append(s1)
    dummystation.append(s2)
    dummystation.append(s3)
    dummystation.append(s4)
    dummystation.append(s5)
    assert inconsistent_typical_range_stations(dummystation) == [s1, s2, s3]