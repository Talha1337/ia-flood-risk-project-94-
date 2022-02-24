from floodsystem.utils import sorted_by_key
def stations_level_over_threshold(stations, tol):
    list_of_over_threshold = [] #initialise empty list
    for station in stations:
        name_and_relative_water = [] #initialise empty list of a station's name and its relative water level
        if station.relative_water_level() == None or station.relative_water_level() > 50: #removes anomalous data, statement after the and is based on judgement
            pass
        elif station.relative_water_level() > tol: #if first if statement is not met, this will trigger.
            name_and_relative_water.append(station.name) 
            name_and_relative_water.append(station.relative_water_level())
            list_of_over_threshold.append(tuple(name_and_relative_water)) #tuple of name and relative water level added to the list.
    return list_of_over_threshold #loop complete, all relative water levels now given in tuples.
def stations_highest_rel_level(stations, N):
    station_list = stations_level_over_threshold(stations, -50) #Form list of stations over an extremely small threshold value, from which it can be reasonably assumed all stations will have a greater water level than this. 
    station_leaderboard = sorted_by_key(station_list, 1, reverse=True) #Sorted based on level of water in station, returning a list of highest to lowest.
    small_station_list = station_leaderboard[0:N] #Take the slice of N indices of the greatest water level stations
    return small_station_list
def stations_level_over_threshold_noname(stations, tol):
    list_of_over_threshold = []
    for station in stations:
        name_and_relative_water = []
        if station.relative_water_level() == None or station.relative_water_level() > 50:
            pass
        elif station.relative_water_level() > tol:
            name_and_relative_water.append(station)
            name_and_relative_water.append(station.relative_water_level())
            list_of_over_threshold.append(tuple(name_and_relative_water))
    return list_of_over_threshold
def stations_highest_rel_level_noname(stations, N):
    station_list = stations_level_over_threshold_noname(stations, -50)
    station_leaderboard = sorted_by_key(station_list, 1, reverse=True)
    small_station_list = station_leaderboard[0:N]
    return small_station_list