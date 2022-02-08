# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


# i dont think this is supposed to be here (what is this?) : from types import NoneType


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    
    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    """Task 1F"""
    def typical_range_consistent(self):
        """Check to see if the output is none, then check to see if the second values"""
        if self.typical_range == None:
            return False
        elif self.typical_range[1] < self.typical_range[0]:
            return False
        else:
            return True
    def relative_water_level(self):

        if self.typical_range == None:
            return None
        elif self.typical_range[0] > self.typical_range[1]:
            return None
        elif self.latest_level == None:
            return None
        else:
            latest_water_level_within_range = self.latest_level - self.typical_range[0]
            typical_water_range = self.typical_range[1] - self.typical_range[0]
            return latest_water_level_within_range/typical_water_range



"""Task 1F"""        
def inconsistent_typical_range_stations(stations):
    """empty list to hold inconsistent stations"""
    inconsistent_list = []
    for station in stations:
        """Checking for inconsistent stations then appending them to the empty list"""
        if station.typical_range_consistent() == False:
            inconsistent_list.append(station)
    return inconsistent_list
